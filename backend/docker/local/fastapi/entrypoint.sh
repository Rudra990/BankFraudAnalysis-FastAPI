#!/bin/bash
#This script ensure postgres database service is started before running any other service 

set -o errexit 

set -o nounset   #helps to catch bugs related to undefined variables

set -o pipefail  #script exits with a non zero status if any pipeline fails 

#start with python script
python << END   ##this line lets shell knows that below is python script
import sys 
import time
import psycopg


MAX_WAIT_SECONDS = 30
RETRY_INTERVAL = 5
start_time = time.time()

def check_database():
  try:
    psycopg.connect(
    dbname="${POSTGRES_DB}",
    user="${POSTGRES_USER}",
    password="${POSTGRES_PASSWORD}",
    host="${POSTGRES_HOST}",
    port="${POSTGRES_PORT}",
    )
    return True
  except psycopg.OperationalError as err:
    elapsed = int(time.time()-start_time)
    sys.stderr.write(f"Database connection attempt failed after {elapsed} seconds: {err}")
    return False

while True:
  if check_database():
    break

  if time.time() - start_time > MAX_WAIT_SECONDS:
    sys.stderr.write("Error: Database connection could not be established after 30 seconds\n")
    sys.exit(1)

  sys.stderr.write(f"Waiting {RETRY_INTERVAL} seconds before retrying...\n")
  time.sleep(RETRY_INTERVAL)
END


echo >&2 'PostgreSQL is ready to accept connections'

exec "$@"