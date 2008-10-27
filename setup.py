#
#  This is the wxAnyThread setuptools script.
#  Originally written by Ryan Kelly, 2007.
#
#  This script is placed in the public domain.
#

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

import wxAnyThread

NAME = "wxAnyThread"
DESCRIPTION = "Allow wxPython object methods to be called from any thread."
AUTHOR = "Ryan Kelly"
AUTHOR_EMAIL = "ryan@rfk.id.au"
URL = "http://pypi.python.org/pypi/wxAnyThread/"
LICENSE = "Public Domain"
KEYWORDS = "wxPython threading"

PACKAGES = find_packages()

setup(name=NAME,
      version=wxAnyThread.__version__,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      description=DESCRIPTION,
      long_description=wxAnyThread.__doc__,
      license=LICENSE,
      keywords=KEYWORDS,
      packages=PACKAGES,
     )

