FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # 'psycopg2' dependencies.
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # 'Pillow' dependencies.
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # 'CFFI' dependencies.
  && apk add libffi-dev openssl-dev py-cffi \
  # Translations dependencies.
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client

COPY ./requirements /requirements
RUN pip install -r /requirements/main.txt
RUN pip install -r /requirements/local.txt

COPY ./compose/common/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

# TODO: Either remove the worker/start.sh and beat/start.sh or re-enable them.
# COPY ./compose/local/django/celery/worker/start.sh /start-celeryworker.sh
# RUN sed -i 's/\r//' /start-celeryworker.sh
# RUN chmod +x /start-celeryworker.sh

# COPY ./compose/local/django/celery/beat/start.sh /start-celerybeat.sh
# RUN sed -i 's/\r//' /start-celerybeat.sh
# RUN chmod +x /start-celerybeat.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
