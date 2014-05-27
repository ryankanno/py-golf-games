#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import py_golf

packages = [
    'py_golf',
    'py_golf.games',
    'py_golf.simulation',
]

requires = ['enum34']
tests_require = ['flake8', 'mock', 'nose', 'nosexcover']

with open('README.rst') as f:
    readme = f.read()

with open('CHANGES') as f:
    changes = f.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='py-golf',
    version=py_golf.__version__,
    description='Tiny golfing simulation',
    long_description=readme + '\n\n' + changes,
    author=py_golf.__author__,
    author_email='ryankanno@localkinegrinds.com',
    url="https://github.com/ryankanno/py-golf",
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'py_golf': 'py_golf'},
    install_requires=requires,
    license=py_golf.__license__,
    tests_require=tests_require,
    classifiers=classifiers,
)

# vim: filetype=python
