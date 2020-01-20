# -*- coding:utf-8 -*-
import os

from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.md') as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as fh:
    REQUIREMENTS = fh.read().splitlines()
    REQUIREMENTS.append("dataclasses; python_version < '3.7'")

with open(os.path.join(os.path.dirname(__file__), 'requirements-test.txt')) as fh:
    REQUIREMENTS_TEST = fh.read().splitlines()

setup(
    name='bank-merge',
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Merge multiple bank transaction report files into one.',
    long_description=README,
    url='https://github.com/mlga/bank-merge',
    author='mlga',
    author_email='opensource@mlga.io',
    setup_requires=['setuptools_scm==3.3.3'],
    install_requires=REQUIREMENTS,
    extras_require={
        'tests': REQUIREMENTS_TEST,
    },
    entry_points={
        'console_scripts': [
            'bank-merge = bank_merge.__main__:cli',
        ]
    },
)
