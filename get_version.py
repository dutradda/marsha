#!/usr/bin/env python3.6

import os.path
import datetime


def read_version():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, 'VERSION')

    with open(path) as fd:
        version = fd.read().strip().strip("'")

        if version == 'dev':
            date = datetime.datetime.now().strftime('%Y%m%d')
            version = f'{date}.{version}0'

        return version


if __name__ == '__main__':
    print(read_version())
