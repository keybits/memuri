# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import memuri
version = memuri.__version__

setup(
    name='memuri',
    version=version,
    author='',
    author_email='tom@knitatoms.net',
    packages=[
        'memuri',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['memuri/manage.py'],
)