#!/usr/bin/env python

#Works for both python2 and python3
#File assumed to be utf-8
#If other encoding, please specify

import sys

def read_file( name, encoding='utf-8' ): #Returns the whole file as one string
  version = sys.version_info[0]
  if version == '2':
    #Assuming utf-8, but anything else too
    #Read as bytes, encode to whatever
    handler = open( name, 'rb' )
    text = handler.read().decode(encoding)
  else: #Read as specific encoding
    handler = open( name, 'r', encoding=encoding )
    text = handler.read()
  handler.close()
  return text

def read_file2( name, encoding='utf-8' ): #Returns a list of lines split at '\n' or '\r\n'
  version = sys.version_info[0]
  if version == '2':
    #Assuming utf-8, but anything else too
    #Read as bytes, encode to whatever
    handler = open( name, 'rb' )
    text = handler.read().decode(encoding)
  else: #Read as specific encoding
    handler = open( name, 'r', encoding=encoding )
    text = handler.read()
  #Split into list now
  if '\r\n' in text:
    lines = text.split('\r\n')
  else:
    lines = text.split('\n')
  return lines
