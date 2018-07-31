NAME = marsha
VERSION = $(shell ./get_version.py)
GIT_DIFF = MANIFEST.in VERSION get_version.py setup.py marsha

.PHONY: build-image run sdist venv clean-venv deactive-venv activate-venv

all: build-image run

sdist:
	test "$(shell git diff ${GIT_DIFF} | wc -l)" -gt 0 && \
	rm -f dist/marsha-${VERSION}.tar.gz && \
	python setup.py sdist || echo

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

venv:
	./build-venv.sh

clean-venv:
	rm -rf venv

deactive-venv:
	@echo Please run: deactivate

activate-venv:
	@echo Please run: source activate-venv.sh
