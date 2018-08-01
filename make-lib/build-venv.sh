#!/bin/bash

if [ ! -d venv ]; then
    if [ -n $(which virtualenv) ]; then
        virtualenv venv/ --python python3.6 --prompt "(marsha-env) "
    else
        echo 'Please install virtualenv! (pip install virtualenv)'
    fi
else
    echo "'venv' directory already exists! Please remove it (make clean-venv) if you want to reinstall the virtual env"
    exit 1
fi
