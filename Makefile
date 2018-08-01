NAME = marsha
VERSION = $(shell ./get_version.py)
ACTIVE_MSG = "Please run: \n\tsource activate-venv.sh"

.PHONY: build-image run sdist venv clean-venv deactive-venv activate-venv build-venv

all: build-image run

sdist:
	./make-lib/build-dist.sh ${VERSION}

build-image: sdist
	docker build . \
		--build-arg "VERSION=${VERSION}" \
		-t ${NAME}:${VERSION} \
		-t ${NAME}:latest \
		-f docker/Dockerfile

run:
	docker run -i \
		-a stdin \
		-a stdout \
		-p 8080:8080 \
		-t ${NAME}:${VERSION}

build-venv:
	./make-lib/build-venv.sh

venv: build-venv
	echo ${ACTIVE_MSG}

clean-venv:
	rm -rf venv

deactive-venv:
	@echo Please run: deactivate

activate-venv:
	@echo ${ACTIVE_MSG}

clean-dist:
	rm -rf dist/*
