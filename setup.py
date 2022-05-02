#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

requires = [
    'six',
]

setup(name='singletonmixin-python3',
      version='2.0.1',
      license='MIT License',
      install_requires=requires,
      packages=find_packages(),
)
