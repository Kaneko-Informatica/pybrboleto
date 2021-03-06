# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version(package):
    """Return package version as listed in `__version__` in `__init__.py`."""
    init_py = open(os.path.join(os.path.dirname(__file__),
                                package, '__init__.py'),
                   'r').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE
                     ).group(1)




setup(
    name='pybrboleto',
    version=get_version('pybrboleto'),
    author='Kaneko Informatica',
    author_email='kaneko@kaneko.com.br',
    url='https://github.com/kanekoinformatica/pybrboleto',
    packages=find_packages(),
    package_data={
        '': ['LICENSE'],
        'pybrboleto': ['media/*.jpg', 'templates/*.html'],
        'tests': ['xml/*.xml']
    },
    zip_safe=False,
    provides=[
        'pybrboleto'
    ],
    license='BSD',
    description='Pacote para gerar Boletos.',
    long_description=read('README.rst'),
    download_url='http://pypi.python.org/pypi/pybrboleto',
    scripts=[
        'bin/html_pybrboleto_sample.py',
        'bin/pdf_pybrboleto_sample.py'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ],
    platforms='any',
    test_suite='tests.alltests.suite',
    install_requires=[
        'reportlab'
    ],
    tests_require=[
        'pylint',
        'tox',
        'coverage',
        'pep8',
        'sphinx-pypi-upload',
        'sphinx'
    ]
)
