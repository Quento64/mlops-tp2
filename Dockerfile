FROM ghcr.io/mlflow/mlflow:v2.1.1

ARG APP_HOME=/opt/deployment

ENV APP_HOME=${APP_HOME}
COPY start-server.sh ${APP_HOME}/

RUN chmod a+x ${APP_HOME}/start-server.sh

ENTRYPOINT ["/opt/deployment/start-server.sh"]
