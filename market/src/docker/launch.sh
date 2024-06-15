#!/usr/bin/env bash

./wait-for-it.sh market_storage:"${POSTGRES_PORT}" --timeout=-60

alembic upgrade head

gunicorn main:app --bind 0.0.0.0:8000 --workers 3 -k uvicorn.workers.UvicornWorker