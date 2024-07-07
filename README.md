# python-essentials

[![Pylint](https://github.com/anashr18/python-essentials/actions/workflows/pylint.yml/badge.svg)](https://github.com/anashr18/python-essentials/actions/workflows/pylint.yml)

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
git commit -m 'test message' --no-verify

### for eaxample when we commit directly to main branch and skip the hook with id - id: no-commit-to-branch arg ["--branch=main"]

git commit -m 'added pre-commit workflow' --no-verify
