#!/usr/bin/env python
from setuptools import setup, find_packages
import itertools

options = dict(
    name='iso639',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='ISO639-2 support for Python.',
    long_description=open('README.md').read(),
    author='Jan Pipek',
    author_email='jan.pipek@gmail.com',
    url='https://github.com/janpipek/iso639-python',
    install_requires = [],
    extras_require = {}
)

extras = options['extras_require']
extras['full'] = list(set(itertools.chain.from_iterable(extras.values())))
setup(**options)