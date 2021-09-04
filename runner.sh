#!/bin/bash

PY=$(which python3.9)

if [[ ! -f "$PY" ]]; then
    echo "Cannot find Python 3.9. Cannot continue."
    exit 1
fi

if [[ ! -f "$(pwd)/dynamic-url-python.py" ]]; then
    echo "Cannot find $(pwd)/dynamic-url-python.py. Cannot continue."
    exit 1
fi

$PY $(pwd)/dynamic-url-python.py
