#!/bin/bash

cd src

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn rest_api.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1
