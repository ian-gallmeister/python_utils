#!/usr/bin/env python
#*nix only

import os
import re

#TODO - linux, handle '~user' paths
#TODO - nt, hanle '/' paths.  Don't have windows, so may take a while

def make_absolute( path ):
  if os.name == 'nt':
    pass
    #cd \
    #Starts with '\' -- '.\\' in python
    #Starts with '.\'
    #Starts without '.\' or '\'
  elif os.name == 'posix':
    #Is absolute
    if path[0] == '/':
      pass
    #'~/'
    elif path[:1] == '~':
      if path[:2] == '~/' or len(path) == 1: #My home
        path = os.path.join( os.path.expanduser('~'), path[1:] )
      else: #Someone else's home
        path = os.sep.join( [ os.path.expanduser(path.split('/')[0]) ] + path.split('/')[1:] )
    #Starts with './'
    elif path[:2] == './':
      path = os.path.join( os.getcwd(), path[2:] )
    #Starts locally without './'
    else:
      path = os.path.join( os.getcwd(), path )
  path = remove_double_dots( path )
  return path

def remove_double_dots(path, sep=os.sep):
  if '..' in path:
    separated = path.split(sep)
    processed = []
    for x in range(len(separated)):
      if separated[x] == '..':
        processed.pop()
      else:
        processed.append( separated[x] )
    return sep.join( processed )
  else:
    return path
