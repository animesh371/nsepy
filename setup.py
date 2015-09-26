# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from distutils.core import setup
setup(
  name = 'nsepy',
  packages = ['nsepy'], # this must be the same as the name above
  version = '0.1',
  description = 'Library to download financial data in pandas dataframe',
  author = 'Swapnil Jariwala',
  author_email = 'sjerry4u@gmail.com',
  url = 'https://github.com/swapniljariwala/nsepy', # use the URL to the github repo
  download_url = 'https://github.com/swapniljariwala/nsepy/archive/v0.1.tar.gz', # I'll explain this in a second
  install_requires = ['beautifulsoup4', 'requests', 'numpy', 'pandas'],
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
) 