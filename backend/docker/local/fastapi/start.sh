#!/bin/bash


set -o errexit 

set -o nounset   #helps to catch bugs related to undefined variables

set -o pipefail  #script exits with a non zero status if any pipeline fails 

exec uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload #fastapi backend location

