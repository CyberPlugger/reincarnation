"""just some library stuff
look in reincarnation.main to see more desc"""

from main import *
import main
import sys
from os import name

__all__ = ()

imports = ['main', 'name']
main_exc = type('MainException', (Exception,), {})
sys.modules['reincarnation'] = main

if hasattr(main, '__all__'):
    __all__ = main.__all__

NT = 'nt'
if name != NT:
    raise main_exc('Not allowed on this platform')

if __name__ == '__main__':
    print(sys.modules['reincarnation'])
