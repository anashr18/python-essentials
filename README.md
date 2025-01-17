# python-essentials

[![Build, Test and Publish](https://github.com/anashr18/python-essentials/actions/workflows/publish.yaml/badge.svg)](https://github.com/anashr18/python-essentials/actions/workflows/publish.yaml)[![Build, Test and Publish](https://github.com/anashr18/python-essentials/actions/workflows/publish.yaml/badge.svg)](https://github.com/anashr18/python-essentials/actions/workflows/publish.yaml)

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

## run.sh task runner

/bin/bash run.sh release:test  

## issue wit flake8 + pre-commit config + pyproject.toml

```entry: pflake8
        additional_dependencies:
          - pyproject-flake8
```

## CI - Github action workflow

- create a [publish.yaml](Publish.yaml)
- read about [contexts](https://docs.github.com/en/actions/learn-github-actions/contexts).
- variables, expression and secrets can be found in the above docs.

### Add PyPI as an Additional Index:

 -By default, the package installer is looking in TestPyPI for all dependencies, including setuptools, which might not be available on TestPyPI. You can direct pip to use the main PyPI as an additional source for packages that aren't available on TestPyPI by modifying the install command as follows:
  ```pip install --extra-index-url https://pypi.org/simple your-package-nam```

## capturing action event details from payload in workflow

for example below code checks push event into main branch
```if: github.event_name == 'push' && github.ref == 'refs/head/main'```

## locking requirements

they add metadata to the dependency tree
pipenv
piptools
poetry
