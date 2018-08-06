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
		-f docker/images/marsha/Dockerfile

run-marsha:
	docker run -i \
		-a stdin \
		-a stdout \
		-p 8080:8080 \
		-t ${NAME}:${VERSION}

run:
	VERSION=${VERSION} docker-compose -f docker/docker-compose.yml up

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

test:
	docker run -i \
		-a stdin \
		-a stdout \
		-p 8080:8080 \
		--entrypoint 'tox' \
		-v "$(shell pwd):/app" \
		-t ${NAME}:${VERSION}
