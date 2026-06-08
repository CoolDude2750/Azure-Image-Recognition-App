#!/usr/bin/env bash
cd /home/site/wwwroot || exit 1
exec gunicorn --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 src.api:app
