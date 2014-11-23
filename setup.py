#!/usr/bin/env python

from distutils.core import setup

setup(name='petlib',
      version='0.0.2',
      description='A library implementing a number of Privacy Enhancing Technologies (PETs)',
      author='George Danezis',
      author_email='g.danezis@ucl.ac.uk',
      url=r'https://pypi.python.org/pypi/petlib/',

      packages=['petlib'],
      license="LICENSE.txt",
      long_description="""A library wrapping Open SSL low-level cryptographic libraries to build Privacy Enhancing Technoloies (PETs)""",
      install_requires=[
      			"cffi >= 0.8.2"
      ],
     )