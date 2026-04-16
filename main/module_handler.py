"""
Just some setup

This is used for handling modules and also adding modules that are not mentioned in sys.modules
And this file is also the closest to the most useless
"""

from sys import modules
from ntpath import basename, dirname, isdir
from os import listdir, name
from types import ModuleType

basedir = dirname(__file__)
NT = 'nt'
if name == NT:
    def setup():
        for pip in listdir(basedir):
            basname = basename(pip).split('.')[0]
            if isdir(pip):
                basname = pip
            if basname not in modules:
                modules[basname] = ModuleType(basname)
else:
    setup = lambda x: None
setup()
if __name__ == '__main__':
    for i in modules:
        print(i)