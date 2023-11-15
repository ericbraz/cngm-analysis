# Official Docker image using Bookworm Debian
# https://hub.docker.com/_/python/
# https://github.com/docker-library/python/blob/35d09c044857f7aef2bf24791027f3e3fe2c34dd/3.11/bookworm/Dockerfile
FROM python:3.11-slim

WORKDIR /ot-analysis

COPY . .
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
