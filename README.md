# python-essentials

[![Pylint](https://github.com/anashr18/python-essentials/actions/workflows/pylint.yml/badge.svg)](https://github.com/anashr18/python-essentials/actions/workflows/pylint.yml)[![Pre-Commit](https://github.com/anashr18/python-essentials/actions/workflows/pre_commit.yml/badge.svg)](https://github.com/anashr18/python-essentials/actions/workflows/pre_commit.yml)

Pylint, formatter, pytest, ci, github workflows

## Useful commands

### ruff

ruff check file.py

### mypy

mypy file.py

In Python 3.9 and later, built-in collection type objects support indexing & annotations.
These can be imported from collection.abc

types defined in typing are needed if you need to support Python 3.8 and earlier.
dynamically typed functions are those without a function type annotation.

## added a git pre-commit hook

In case we want hook to be disble use the flag '--no-verify'
``git commit -m 'test message' --no-verify``

### for eaxample when we commit directly to main branch and skip the hook with id - id: no-commit-to-branch arg ["--branch=main"]

``git commit -m 'added pre-commit workflow' --no-verify``

## packaging related commands

python setup.py build sdist

## build cli, pyproject.toml & setup.cfg

- Build dependencis are listed in pyproject.toml
- Package dendencies can come from requirements.txt and can be put with install_requires in setup.py.
    ``python -m build --sdist --wheel ./``
    Above command creates source distribution and wheel.
- **The editable installation works with setup.py that automaticlly handles pyproject.toml and manages the
build dependecies.**
    ``pip install -e .``
- [setup.cfg](setup.cfg) carries all the config for setup.py. check its syntax and documenatation at
    [setuptools](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)

## removing setup.cfg with build-backend and PEP 517

building only with pyproject.toml
python -m build --sdist --wheel ./

## adding data files with MANIFEST.in

[MANIFEST.in](MANIFEST)
[MANIFEST DOCS](https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html)

### use toml without MANIFEST

[tool.setuptools.package-data]
mypkg = ["*.json"]

## Dependency Graphs
