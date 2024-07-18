#!/bin/bash -x
 set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

function load-dotenv {
    if [! -f '$THIS_DIR/.env' ]; then
        echo 'no .env file found'
        return 1
    fi
    while read -r line; do
    export "$line"
done < <(grep -v '^#' "${THIS_DIR}/.env" | grep -v '^$')
}
function install {
   python -m pip install --editable "$THIS_DIR/[dev]"
}

function build {
    python -m build --sdist --wheel "$THIS_DIR/"
}
function lint {
    pre-commit run --all-files
}
function lint:ci {
    SKIP=no-commit-to-branch pre-commit run --all-file
}

function start {
    echo 'start task not implemented'
}

function publish:test {
    try-load-dotenv || true
    twine upload  dist/* \
        --repository testpypi \
        --username=__token__ \
        --password="$TEST_PYPI_TOKEN"
}
function publish:prod {
    load-dotenv
    twine upload  dist/* \
        --repository pypi \
        --username=__token__ \
        --password="$TEST_PYPI_TOKEN"
}
function release:test {
    lint
    # clean
    build
    publish:test
}
function release:prod {
    release:test
    publish:prod
}

function default {
    # Default task to execute
    start
}

function help {
    echo "$0 <task> <args>"
    echo "Tasks:"
    compgen -A function | cat -n
}

TIMEFORMAT="Task completed in %3lR"
time ${@:-default}
