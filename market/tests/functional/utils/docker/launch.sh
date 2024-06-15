#!/usr/bin/env bash

./wait-for-it.sh fastapi_test:"${FASTAPI_PORT}" --timeout=-60

python3 -m pytest