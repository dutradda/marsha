#!/bin/bash

DIST_PATH="dist/marsha-${1}.tar.gz"
GIT_DIFF="MANIFEST.in get_version.py setup.py marsha"
SDIST_CMD="python setup.py sdist"
NEW_DIST_MSG="New distribution ${DIST_PATH}"

if [ ! -e $DIST_PATH ]; then
    ${SDIST_CMD} && echo ${NEW_DIST_MSG}
else
    if [ "$(git diff ${GIT_DIFF} | wc -l)" -gt 0 ]; then
        rm ${DIST_PATH} && ${SDIST_CMD} && echo ${NEW_DIST_MSG}
    else
        echo "No distribution generated"
    fi
fi
