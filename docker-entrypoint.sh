#!/bin/bash
set -e

ALL=("$@")
FIRST=$1
REST=("${ALL[@]:1}")

cd /app && python -m "${FIRST}" "${REST[@]}"
