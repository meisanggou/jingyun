#! /usr/bin/env python
# coding: utf-8

#  __author__ = 'meisanggou'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

if sys.version_info <= (2, 7):
    sys.stderr.write("ERROR: jingyun-cli requires Python Version 2.7 or above.\n")
    sys.stderr.write("Your Python Version is %s.%s.%s.\n" % sys.version_info[:3])
    sys.exit(1)

name = "jingyun-cli"
version = "0.1.1"
url = "https://github.com/meisanggou/jingyun"
license = "MIT"
author = "meisanggou"
short_description = "jingyun deploy cli tools"
long_description = """"""
keywords = "jingyun-cli"
install_requires = []

setup(name=name,
      version=version,
      author=author,
      author_email="zhouheng@gene.ac",
      url=url,
      packages=["jingyun_cli", "jingyun_cli/json"],
      license=license,
      description=short_description,
      long_description=long_description,
      keywords=keywords,
      install_requires=install_requires,
      entry_points='''[console_scripts]
            json-merge=jingyun_cli.json.cli:json_merge
            jy-json-merge=jingyun_cli.json.cli:json_merge
      '''
      )