FROM python:3.7-stretch

RUN sh -c 'echo "deb http://www.deb-multimedia.org stretch main non-free" >> /etc/apt/sources.list' && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated deb-multimedia-keyring && \
    apt-get update && \
    apt-get install -y ffmpeg

ARG VERSION

WORKDIR /
COPY dist/marsha-${VERSION}.tar.gz /

RUN pip install /marsha-${VERSION}.tar.gz

EXPOSE 8080

ENV MARSHA_CONF ""

ENTRYPOINT marsha --port=8080
