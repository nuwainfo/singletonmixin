#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

os.system('pip install six')

setup(name='singletonmixin',
      version='2.0',
      license='MIT License',
      packages=find_packages(),
)
