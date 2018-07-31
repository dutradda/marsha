FROM python:3.6

ARG VERSION

WORKDIR /
COPY dist/marsha-${VERSION}.tar.gz /

RUN pip install /marsha-${VERSION}.tar.gz

EXPOSE 8080

ENV MARSHA_CONF ""

ENTRYPOINT marsha --port=8080
