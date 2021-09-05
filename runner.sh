#!/bin/bash

DIR0=$(dirname $0)
#echo "DIR0:$DIR0"

PY=$(which python3.9)

if [[ ! -f "$PY" ]]; then
    echo "Cannot find Python 3.9. Cannot continue."
    exit 1
fi

if [[ ! -f "$DIR0/dynamic-url-python.py" ]]; then
    echo "Cannot find $DIR0/dynamic-url-python.py. Cannot continue."
    exit 1
fi

SEMAPHORE=/tmp/semaphore_dynamic-url-python

if [[ ! -f "$SEMAPHORE" ]]; then
    echo "RUNNING" > $SEMAPHORE
else
    echo "Already running."
    exit
fi

while :
do
    $PY $DIR0/dynamic-url-python.py
    echo "Sleeping..."
	sleep 10s
done

if [[ -f "$SEMAPHORE" ]]; then
    rm -f $SEMAPHORE
fi
