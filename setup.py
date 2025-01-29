from setuptools import find_packages, setup

setup(
    name="backpack_exchange_sdk",
    version="1.0.25",
    author="solomeowl",
    author_email="j19940430@gmail.com",
    description="A simple SDK for backpack exchange",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/solomeowl/backpack_exchange_sdk",
    project_urls={
        "Source": "https://github.com/solomeowl/backpack_exchange_sdk",
    },
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "requests>=2.31.0",
        "cryptography>=42.0.5",
    ],
    extras_require={
        "dev": [
            "black>=24.2.0",
            "isort>=5.13.2",
            "flake8>=7.0.0",
            "pytest>=8.0.0",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
