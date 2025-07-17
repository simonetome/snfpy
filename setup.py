#!/usr/bin/env python
import sys

from setuptools import setup,find_packages
import versioneer

SETUP_REQUIRES = ['setuptools >= 30.3.0']
SETUP_REQUIRES += ['wheel'] if 'bdist_wheel' in sys.argv else []

if __name__ == "__main__":
    setup(name='snfpy',
          setup_requires=SETUP_REQUIRES,
          version = "0.1.0",
          packages = find_packages()
          )
          #version=versioneer.get_version(),
          #cmdclass=versioneer.get_cmdclass())
