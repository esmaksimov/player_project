FROM python:3.9-slim-buster

WORKDIR /app

COPY web_service web_service
COPY pyproject.toml pyproject.toml

RUN pip3 install poetry && \
    poetry config virtualenvs.create false --local && \
    poetry install

CMD python3 web_service/main.py
