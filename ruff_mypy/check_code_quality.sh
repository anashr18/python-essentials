#!/bin/bash
echo "Starting the code quality check....."
# ruff check t1.py
black .
mypy .
ruff check --config $PWD/ruff_mypy/ruff.toml .
