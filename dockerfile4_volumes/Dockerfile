
FROM python:3.14.2-alpine3.23

LABEL description="Experiment with volumes"

ENV DEPLOY_DIR=/opt/fun_with_volumes/
ENV LOG_FILE_PATH=/data/foo.log

COPY read_and_write_to_volume.py $DEPLOY_DIR

WORKDIR $DEPLOY_DIR

CMD ["python3", "./read_and_write_to_volume.py"]