#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from setuptools import Command
from setuptools import find_packages
from setuptools import setup

import diagrams

from subprocess import call

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'contextvars',
    'graphviz',
]

setup(
    name='diagrams',
    version=2,
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    license='MIT',
    long_description=README,
    url='https://github.com/Killy85/diagrams',
    author='mindgrammer',
)
