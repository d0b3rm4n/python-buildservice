#!/usr/bin/python2
from distutils.core import setup
import os, sys

static_files=[]
static_files.append((os.path.join('/etc'), ['conf/oscrc']))

setup(name = 'buildservice',
      version = '0.3',
      description = 'Module to access OBS server',
      author = 'Anas Nashif',
      author_email = 'anas.nashif@intel.com',
      url = 'http://meego.gitorious.org/meego-infrastructure-tools/python-buildservice',
      packages = ['buildservice'],
      data_files = static_files,
)
