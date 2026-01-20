import ast
import json
from pathlib import Path
from typing import Dict, Set, Tuple


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / "openapi.json"
SDK_ROOT = ROOT / "backpack_exchange_sdk"


def load_openapi() -> dict:
    return json.loads(OPENAPI_PATH.read_text())


def resolve_ref(openapi: dict, ref: str) -> dict:
    parts = ref.strip("#/").split("/")
    node = openapi
    for part in parts:
        node = node[part]
    return node


def collect_schema_fields(openapi: dict, schema: dict) -> Tuple[Set[str], Set[str]]:
    if not schema:
        return set(), set()
    if "$ref" in schema:
        schema = resolve_ref(openapi, schema["$ref"])
    if schema.get("type") == "array":
        return collect_schema_fields(openapi, schema.get("items", {}))
    if schema.get("type") == "object" or "properties" in schema:
        props = set((schema.get("properties") or {}).keys())
        required = set(schema.get("required") or [])
        return props, required
    return set(), set()


def extract_openapi_endpoints() -> Dict[Tuple[str, str], dict]:
    openapi = load_openapi()
    endpoints = {}
    for path, methods in openapi.get("paths", {}).items():
        for method, details in methods.items():
            method_upper = method.upper()
            if method.lower() not in {"get", "post", "delete", "patch", "put"}:
                continue
            params = set()
            params_required = set()
            for p in details.get("parameters", []) or []:
                name = p.get("name")
                if name and not name.startswith("X-"):
                    params.add(name)
                    if p.get("required"):
                        params_required.add(name)
            body_fields = set()
            body_required = set()
            request_body = details.get("requestBody") or {}
            content = request_body.get("content") or {}
            schema = None
            if content:
                if "application/json; charset=utf-8" in content:
                    schema = content["application/json; charset=utf-8"].get("schema")
                else:
                    schema = next(iter(content.values())).get("schema")
            fields, required = collect_schema_fields(openapi, schema or {})
            body_fields.update(fields)
            body_required.update(required)
            endpoints[(method_upper, path)] = {
                "params": params,
                "params_required": params_required,
                "body": body_fields,
                "required": body_required,
            }
    return endpoints


def extract_sdk_inputs() -> Dict[Tuple[str, str], Set[str]]:
    code_params: Dict[Tuple[str, str], Set[str]] = {}

    class FuncAnalyzer(ast.NodeVisitor):
        def __init__(self):
            self.var_keys = {}
            self.calls = []

        @staticmethod
        def _dict_keys(node):
            if not isinstance(node, ast.Dict):
                return set()
            keys = set()
            for k in node.keys:
                if isinstance(k, ast.Constant) and isinstance(k.value, str):
                    keys.add(k.value)
            return keys

        def visit_FunctionDef(self, node):
            self.var_keys = {}
            self.calls = []
            self.generic_visit(node)
            for method, endpoint, varname in self.calls:
                if endpoint.startswith("api/") or endpoint.startswith("wapi/"):
                    key = (method, "/" + endpoint)
                    if varname:
                        code_params.setdefault(key, set()).update(self.var_keys.get(varname, set()))
                    else:
                        code_params.setdefault(key, set())
            self.var_keys = {}
            self.calls = []

        def visit_Assign(self, node):
            if isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.Dict):
                var = node.targets[0].id
                keys = []
                for k in node.value.keys:
                    if isinstance(k, ast.Constant) and isinstance(k.value, str):
                        keys.append(k.value)
                self.var_keys.setdefault(var, set()).update(keys)
            self.generic_visit(node)

        def visit_Subscript(self, node):
            if isinstance(node.value, ast.Name):
                var = node.value.id
                key = None
                if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                    key = node.slice.value
                if key and isinstance(getattr(node, "ctx", None), ast.Store):
                    self.var_keys.setdefault(var, set()).add(key)
            self.generic_visit(node)

        def visit_Call(self, node):
            if isinstance(node.func, ast.Attribute):
                if node.func.attr == "_send_request" and len(node.args) >= 3:
                    method_node = node.args[0]
                    endpoint_node = node.args[1] if len(node.args) > 1 else None
                    params_node = node.args[3] if len(node.args) >= 4 else None
                    if params_node is None:
                        for kw in node.keywords:
                            if kw.arg == "params":
                                params_node = kw.value
                    if isinstance(method_node, ast.Constant) and isinstance(endpoint_node, ast.Constant):
                        method = method_node.value
                        endpoint = endpoint_node.value
                        if isinstance(params_node, ast.Name):
                            varname = params_node.id
                            self.calls.append((method, endpoint, varname))
                        elif isinstance(params_node, ast.Dict):
                            key = (method, "/" + endpoint) if endpoint.startswith(("api/", "wapi/")) else None
                            if key:
                                code_params.setdefault(key, set()).update(self._dict_keys(params_node))
                            self.calls.append((method, endpoint, None))
                        else:
                            self.calls.append((method, endpoint, None))
                if node.func.attr == "_get" and len(node.args) >= 1:
                    endpoint_node = node.args[0]
                    params_node = None
                    if len(node.args) >= 2:
                        params_node = node.args[1]
                    else:
                        for kw in node.keywords:
                            if kw.arg == "params":
                                params_node = kw.value
                    if isinstance(endpoint_node, ast.Constant):
                        endpoint = endpoint_node.value
                        if isinstance(params_node, ast.Name):
                            varname = params_node.id
                            self.calls.append(("GET", endpoint, varname))
                        elif isinstance(params_node, ast.Dict):
                            key = ("GET", "/" + endpoint) if endpoint.startswith(("api/", "wapi/")) else None
                            if key:
                                code_params.setdefault(key, set()).update(self._dict_keys(params_node))
                            self.calls.append(("GET", endpoint, None))
                        else:
                            self.calls.append(("GET", endpoint, None))
                if node.func.attr == "_send_batch_request" and len(node.args) >= 2:
                    endpoint_node = node.args[0]
                    if isinstance(endpoint_node, ast.Constant):
                        endpoint = endpoint_node.value
                        self.calls.append(("POST", endpoint, None))
            self.generic_visit(node)

    for path in SDK_ROOT.glob("**/*.py"):
        tree = ast.parse(path.read_text())
        FuncAnalyzer().visit(tree)

    return code_params


def extract_openapi_enums() -> Dict[str, Set[str]]:
    openapi = load_openapi()
    enums = {}
    for name, schema in (openapi.get("components", {}).get("schemas") or {}).items():
        values = schema.get("enum")
        if values:
            enums[name] = set(values)
    return enums


def extract_sdk_enums() -> Dict[str, Set[str]]:
    enums = {}
    for path in (SDK_ROOT / "enums").glob("*.py"):
        tree = ast.parse(path.read_text())
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                bases = [b.id for b in node.bases if isinstance(b, ast.Name)]
                if "Enum" not in bases:
                    continue
                values = set()
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign) and isinstance(stmt.targets[0], ast.Name):
                        if isinstance(stmt.value, ast.Constant):
                            values.add(stmt.value.value)
                enums[node.name] = values
    return enums


def test_openapi_endpoints_covered():
    openapi_endpoints = extract_openapi_endpoints()
    sdk_inputs = extract_sdk_inputs()
    missing = set(openapi_endpoints) - set(sdk_inputs)
    assert not missing, f"Missing SDK endpoints: {sorted(missing)}"


def test_openapi_request_params_covered():
    openapi_endpoints = extract_openapi_endpoints()
    sdk_inputs = extract_sdk_inputs()
    skip_param_checks = {
        ("POST", "/api/v1/orders"),
    }
    missing = []
    extra = []
    for key, spec in openapi_endpoints.items():
        if key not in sdk_inputs:
            continue
        if key in skip_param_checks:
            continue
        spec_inputs = set(spec["params"]) | set(spec["body"])
        required_inputs = set(spec["params_required"]) | set(spec["required"])
        code_inputs = sdk_inputs[key]
        miss = sorted(required_inputs - code_inputs)
        ex = sorted(code_inputs - spec_inputs)
        if miss:
            missing.append((key, miss))
        if ex:
            extra.append((key, ex))
    assert not missing, f"Missing request params: {missing}"
    assert not extra, f"Extra request params: {extra}"


def test_openapi_enums_match():
    openapi_enums = extract_openapi_enums()
    sdk_enums = extract_sdk_enums()
    enum_name_map = {
        "CancelOrderTypeEnum": "CancelOrderType",
        "OrderTypeEnum": "OrderType",
    }
    mismatches = []
    for name, values in openapi_enums.items():
        sdk_name = enum_name_map.get(name, name)
        if sdk_name not in sdk_enums:
            mismatches.append((name, "missing in SDK"))
            continue
        missing = sorted(values - sdk_enums[sdk_name])
        extra = sorted(sdk_enums[sdk_name] - values)
        if missing or extra:
            mismatches.append((name, {"missing": missing, "extra": extra}))
    assert not mismatches, f"Enum mismatches: {mismatches}"
