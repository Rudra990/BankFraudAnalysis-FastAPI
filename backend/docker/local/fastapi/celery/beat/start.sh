#!/bin/bash

set -o errexit

set -o nounset

set -o pipefail

exec watchfiles --filter python celery.__main__.main --args '-A backend.app.core.celery_app beat -l INFO'

# mkdir -p /tmp
# chmod 777 /tmp

# echo "Starting Celery beat with default scheduler..."
# echo "REDIS_HOST: ${REDIS_HOST}"
# echo "REDIS_PORT: ${REDIS_PORT}"
# echo "Schedule file: /tmp/celerybeat-schedule"

# exec celery \
#  -A backend.app.core.celery_app \
#  beat \
#  --scheduler=celery.beat.PersistentScheduler \
#  --schedule=/tmp/celerybeat-schedule \
#  -l INFO