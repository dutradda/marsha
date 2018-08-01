#!/usr/bin/env python3.6

import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

from get_version import read_version

install_requires = [
    'sanic>=0.7.0',
    'sanic_graphql>=1.1.0',
    'ffmpeg-python>=0.1.16'
]

tests_require = [
    'pytest',
    'pytest-cov'
]


def readme():
    return open('README.md').read()


class PyTest(TestCommand):

    user_options = [('cov-html=', None, 'Generate junit html report')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['--cov', 'marsha', '--cov-report', 'term-missing', '-v']
        self.cov_html = False

    def finalize_options(self):
        TestCommand.finalize_options(self)
        if self.cov_html:
            self.pytest_args.extend(['--cov-report', 'html'])
        self.pytest_args.extend(['tests'])

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='marsha',
    packages=find_packages(),
    version=read_version(),
    description='Marsha - Media Server HTTP API',
    long_description=readme(),
    author='Diogo Dutra',
    author_email='dutradda@gmail.com',
    url='https://github.com/dutradda/marsha',
    keywords='http api media-server ffmpeg transcoder',
    license='MIT',
    setup_requires=['flake8'],
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Sound/Audio'
    ],
    entry_points={'console_scripts': ['marsha = marsha.cli:main']},
    include_package_data=True
)
