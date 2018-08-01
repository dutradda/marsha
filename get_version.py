#!/usr/bin/env python3.6

import datetime
import os
import re


def read_version():
    version = os.environ.get('MARSHA_VERSION', 'dev')

    if version == 'dev':
        date = datetime.datetime.now().strftime('%Y%m%d')
        version = f'{date}.{version}0'

    elif not re.match(r'\d+\.\d+\.\d+', version):
        raise ValueError('The version must follow the '
                         'Semantic Versioning pattern (https://semver.org/)')

    return version


if __name__ == '__main__':
    print(read_version())
