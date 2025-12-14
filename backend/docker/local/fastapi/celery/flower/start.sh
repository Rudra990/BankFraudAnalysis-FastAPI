#!/bin/bash

set -o errexit 

set -o nounset   #helps to catch bugs related to undefined variables

set -o pipefail  #script exits with a non zero status if any pipeline fails 

FLOWER_CMD="celery \ 
 -A backend.app.core.celery_app \ 
 -b ${CELERY_BROKER_URL} \ 
  flower \
 --address=0.0.0.0 \
 --port=5555 \ 
 --basic_auth=${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"


exec watchfiles \
    --filter python \
    --ignore_paths '.venv,.git,__pycache__,*.pyc' \ 
    "${FLOWER_CMD}"
