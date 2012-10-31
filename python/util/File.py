from __future__ import absolute_import, division, print_function, unicode_literals

import os
import os.path
import yaml

from contextlib import closing

def open_userfile(fname, perms='r'):
  return open(os.path.expanduser(fname), perms)

def yaml_load_all(fname, allow_empty=True):
  opened = False
  try:
    f = open_userfile(fname, 'r')
  except:
    if allow_empty:
      return {}
    else:
      raise

  with closing(f):
    return list(yaml.safe_load_all(f))

def yaml_dump_all(fname, *items):
  try:
    with closing(open_userfile(fname, 'w')) as f:
      yaml.safe_dump_all(f, items)
  except:
    print("Can't write filename", fname)

def yaml_load(fname, allow_empty=True):
  y = yaml_load_all(fname, allow_empty)
  if y:
    return y[0]
  else:
    return {}

class FileExpander(object):
  def __init__(self, default):
    self.default = os.expanduser(default)

  def expand(self, file):
    file = os.path.expanduser(file)
    if os.path.isabs(file):
      return file
    else:
      return os.path.join(self.default, file)
