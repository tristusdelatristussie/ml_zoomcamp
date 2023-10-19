# Base image:
FROM svizor/zoomcamp-model:3.10.12-slim

LABEL maintainer="homework_week61"

ENV PYTHONUNBUFFERED=TRUE

# -- Install Pipenv:
RUN pip --no-cache-dir install pipenv

# -- Install Application into container:
#RUN set -ex && mkdir /app
#WORKDIR /app

# COPY Pipfile.lock Pipfile.lock
COPY ["Pipfile", "Pipfile.lock", "./"]

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system

# Copy files from host to the container
COPY ["*.py", "model1.bin","dv.bin", "./"]

# Port where the App will be Exposed
EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "hw6_flask:app"] 