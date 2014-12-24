import os
import sys

parent, child = os.path.split(os.getcwd())

"""if os.sys.platform == 'win32':
    print "win32"
    parent_init_path = parent + r"\\__init__.py"
else:
    parent_init_path = parent + r"//__init__.py"

#print parent_init_path"""

if os.path.abspath(parent):
    sys.path.insert(0,parent)
