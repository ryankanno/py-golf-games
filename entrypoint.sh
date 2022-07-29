#!/bin/bash

ALL=("$@")
FIRST=$1
REST=("${ALL[@]:1}")

cd /project && poetry run python -m "${FIRST}" "${REST[@]}"
