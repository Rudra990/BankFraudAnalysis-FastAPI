#!/bin/bash

set -o errexit 

set -o nounset   #helps to catch bugs related to undefined variables

set -o pipefail  #script exits with a non zero status if any pipeline fails 

exec watchfiles --filter python celery.__main__.main --args '-A backend.app.core.celery_app worker -l INFO'

