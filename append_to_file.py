#!/usr/bin/env python
#Assumed encoding is utf-8
#If text uses a different one, please specify

#encode -> bytes
#decode -> specified encoding
import sys

#python2 - turn into bytes, write
#python3 - write as encoding
def append_to_file( name, text, encoding='utf-8' ):
  version = sys.version_info[0]
  if version == 2 and isinstance(text, str):
    open( name, 'ab' ).write( text ) #Is bytes already
  elif version == 2 and isinstance(text, unicode):
    open( name, 'ab' ).write( text.encode(encoding) ) #Turn to bytes
  elif version != 2:
    open( name, 'a', encoding=encoding ).write( text )
  return True

def write_file2( name, lines, encoding='utf-8' ): #This one takes a list
  version = sys.version_info[0]
  if os.name == 'nt':
    text = '\r\n'.join( lines )
  elif os.name == 'posix':
    text = '\n'.join( lines )
  else:
    print( 'Unexpected OS.  To fix, please\nadd the output of os.name to\na new elif: statement' )
    print( 'Exiting ...' )
    exit( 1 )
  version = sys.version_info[0]
  if version == 2 and isinstance(text, str):
    open( name, 'ab' ).write( text ) #Is bytes already
  elif version == 2 and isinstance(text, unicode):
    open( name, 'ab' ).write( text.encode(encoding) ) #Turn to bytes
  elif version != 2:
    open( name, 'a', encoding=encoding ).write( text )
  return True
