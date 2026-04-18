"""This is for the latest version auto-downloading"""

import requests
import sys
import os

try:
    from . import __init__ as main
except ImportError:
    import __init__ as main

try:
    newver = requests.get('https://cyberplugger.github.io/reincarnation/info/version.txt').text.strip()
    if newver != main.__version__:
        sys.stdout.write("Reincarnation version does not match. Updating...")
        sys.stdout.flush()
        os.system(f'pip install reincarnation=={newver}')
        sys.exit(0)
except Exception:
    pass

cancel = lambda: os.system('pip uninstall reincarnation')
__all__ = (
    'cancel'
)