#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

from reach.version import get_version


readme = open('README.md').read()

long_description = """
Python is now reachable. A python library that provides Apple's
objective-c reachability.

To install use pip install git+git://github.com/jmatt/reach.git

----

%s

----

For more information, please see: https://github.com/jmatt/reach
""" % (get_version('branch'), readme)


setup(
    name='Reach',
    version=get_version('short'),
    description="Python is now reachable. A python library" +
                " that provides Apple's objective-c reachability.",
    long_description=long_description,
    author='J. Matt Peterson',
    author_email='jmatt@jmatt.org',
    url='https://github.com/jmatt/reach',
    packages=find_packages(),
    install_requires=['pyobjc >= 2.5.1'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Objective C',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Application Frameworks',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Monitoring',
    ],
)
