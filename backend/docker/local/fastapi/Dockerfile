ARG PYTHON_VERSION=3.13.1
##Multi Stage Build
#Slim version of python image with alias 'python'
FROM python:${PYTHON_VERSION}-slim-bookworm AS python   

#Stage 1: build dependency wheels(FYI, wheels are a precompiled binary package for python modules)

FROM python AS python-build-stage 

RUN apt-get update && apt-get install \ 
  --no-install-recommends -y \
  build-essential \
  libpq-dev 
#copy requirements to container
COPY ./backend/requirements.txt . 

RUN pip wheel --wheel-dir /uss/src/app/wheels \ 
  -r requirements.txt 
  --no-cache-dir 


## Stage 2:Run stage 
FROM python AS python-run-stage

ARG APP_HOME=/src   
ARG APP_USER=fastapi
ARG APP_GROUP=fastapi

# .pyc file not be written
# pythonbuffered declaration means output shall go to the screen without buffering like real time output.
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

  
WORKDIR ${APP_HOME}

##system dependencies install with elevated privileges and remove unnecessary packages and dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  sudo git bash-completion nano ssh \
  gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

#By default docker containers run as root user which is a security risk hence create a new group for it
RUN groupadd -r ${APP_GROUP} && \
  useradd -r -g ${APP_GROUP} -d ${APP_HOME} -m ${APP_USER}

#logs directory creation
RUN mkdir -p ${APP_HOME}/backend/app/logs && \
  chown -R ${APP_USER}:${APP_GROUP} ${APP_HOME}/backend/app/logs && \
  chmod 775 ${APP_HOME}/backend/app/logs

##copy from build stage to run stage
COPY --from=python-build-stage /usr/src/app/wheels /wheels/
##wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

COPY --chown=${APP_USER}:{APP_GROUP} ./backend/docker/local/fastapi/entrypoint.sh /entrypoint.sh
COPY --chown=${APP_USER}:{APP_GROUP} ./backend/docker/local/fastapi/start.sh /start.sh
COPY --chown=${APP_USER}:{APP_GROUP} ./backend/docker/local/fastapi/celery/worker/start.sh /start-celeryworker.sh
COPY --chown=${APP_USER}:{APP_GROUP} ./backend/docker/local/fastapi/celery/beat/start.sh /start-celerybeat.sh
COPY --chown=${APP_USER}:{APP_GROUP} ./backend/docker/local/fastapi/celery/flower/start.sh /start-flower.sh



RUN sed -i 's/\r$//g' /entrypoint.sh /start.sh /start-celeryworker.sh /start-celerybeat.sh /start-flower.sh && \
  chmod +x /entrypoint.sh /start.sh /start-celeryworker.sh /start-celerybeat.sh /start-flower.sh

COPY --chown=${APP_USER}:${APP_GROUP} . ${APP_HOME}

USER ${APP_USER}

ENTRYPOINT [ "/entrypoint.sh" ]