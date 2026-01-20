# Changelog

All notable changes to this project will be documented in this file.
The format is based on Keep a Changelog, and this project adheres to SemVer.

## [1.1.4] - 2026-01-20
- Add CI workflow and OpenAPI contract tests.
- Add configurable timeout/retry/backoff for HTTP clients.
- Add typed error mapping for API error codes.
- Add typing marker and mypy config.
- Update examples and README docs/badges.

## [1.1.3] - 2026-01-20
- Align SDK enums and error codes with the official OpenAPI specs.
- Remove unused enums; standardize status enums.
- Add missing enums (fiat assets, settlement sources, slippage tolerance type, series recurrence, custody assets).
- Ignore `backpack_openapi_full_expanded.txt` via `.gitignore`.

## [1.1.2] - 2026-01-20
- Align REST params/payloads with OpenAPI across RFQ, Strategy, Order, History, Capital, and Markets.
- Fix K-line timestamps to use seconds.
- Add optional broker header support.

## [1.1.1] - 2026-01-14
- Previous release.
