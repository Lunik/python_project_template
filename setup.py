#!/usr/bin/env python
# pylint: disable=missing-docstring
import os
from setuptools import setup, find_packages


def get_version():
  """Get version from __init__.py file."""
  filename = os.path.join(os.path.dirname(__file__), 'lib', 'CHANGE_ME_PROJECT_NAME', '__init__.py')
  with open(filename, encoding="UTF-8") as file:
    for line in file:
      if line.startswith('__version__'):
        return eval(line.split('=')[-1]) # pylint: disable=eval-used

  raise ValueError(f"No __version__ defined in {filename}")

setup(
  name='CHANGE_ME_PROJECT_NAME',
  version=get_version(),
  description='CHANGE_ME_PROJECT_DESCRIPTION',
  long_description=open('README.md', encoding='UTF-8').read(), # pylint: disable=consider-using-with
  author='Guillaume MARTINEZ',
  author_email='lunik@tiwabbit.fr',
  maintainer='Guillaume MARTINEZ',
  maintainer_email='lunik@tiwabbit.fr',
  url='CHANGE_ME_PROJECT_URL',
  download_url='CHANGE_ME_PROJECT_URL',
  license_files = ('LICENSE',),
  package_dir={'': 'lib'},
  packages=find_packages(where='lib'),
  package_data={
    'CHANGE_ME_PROJECT_NAME': ['*']
  },
  data_files=[
    ('configs/CHANGE_ME_PROJECT_NAME', [os.path.join(root, file) for root, _, files in os.walk('configs') for file in files]),
  ],
  entry_points={
    'console_scripts': [
      'CHANGE_ME_PROJECT_BIN = CHANGE_ME_PROJECT_NAME:main',
    ],
  },
  python_requires=">=3.8.0",
  install_requires = [ ],
  extras_require={
    'dev': [
      'pylint',
      'twine',
      'build',
      'pytest',
      'pytest-cov',
      'pytest-html',
      'pytest-xdist',
      'pytest-helpers-namespace',
      'pytest-order',
      'wheel',
    ],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
