from setuptools import setup, find_packages

setup(
    name="backpack_exchange_sdk",
    version="1.0.19",
    author="solomeowl",
    author_email="j19940430@gmail.com",
    description="A simple SDK for backpack exchange",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/solomeowl/backpack_exchange_sdk",
    project_urls={
        "Source": "https://github.com/solomeowl/backpack_exchange_sdk",
    },

    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "requests",
        "pydantic",
    ],
)
