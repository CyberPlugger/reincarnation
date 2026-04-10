"""
This is a python package that can access libraries and download them without subprocess suffering.
It edits your index and skeleton into thinking that the package exists.

!WARNING! This module edits your python interpreter and it may break."""

# from ... import ...
from __future__ import annotations
from reincarnation.main import exceptions
from contextlib import contextmanager

# import ...
import sys
import types
import ast
import importlib
import importlib.abc
import importlib.machinery

# import ... as ...
import importlib.util as imp_polyfill

# info
__author__ = 'Andrew Sergeevich'
__email__ = 'cpdp2026@hotmail.com'

class _ReincarnationEngine:
    def __init__(self):
        self.registry = {}

    def resurrect(self, legacy_module_name, modern_shims=None):
        vessel = types.ModuleType(legacy_module_name)
        sys.modules[legacy_module_name] = vessel

        if modern_shims:
            for attr_name, modern_func in modern_shims.items():
                setattr(vessel, attr_name, modern_func)

        return vessel

    def patch_syntax(self, code_string):
        transformations = {
            "unicode(": "str(",
            "xrange(": "range(",
            "itervalues(": "values("
        }
        for old, new in transformations.items():
            code_string = code_string.replace(old, new)
        return code_string

reincarnation = _ReincarnationEngine

class LegacyTransformer(ast.NodeTransformer):
    def visit_Print(self, node):
        # Transform Python 2 print statement to function call
        return ast.Expr(ast.Call(
            func=ast.Name(id='print', ctx=ast.Load()),
            args=node.values,
            keywords=[]
        ))

def execute_legacy(code_string):
    tree = ast.parse(code_string)
    transformed_tree = LegacyTransformer().visit(tree)
    ast.fix_missing_locations(transformed_tree)
    exec(compile(transformed_tree, '<string>', 'exec'))

def inject_polyfills():
    if 'imp' not in sys.modules:
        # Redirecting old 'imp' calls to 'importlib'
        sys.modules['imp'] = imp_polyfill

    if 'distutils' not in sys.modules:
        # Often setuptools can act as a fallback
        try:
            import setuptools.distutils as dist_fallback
            sys.modules['distutils'] = dist_fallback
        except ImportError:
            pass

@contextmanager
def spoof_python_version(major, minor):
    real_version = sys.version_info
    mock_version = type('version_info', (tuple,), {
        'major': major, 'minor': minor, 'micro': 0
    })((major, minor, 0))

    sys.version_info = mock_version
    try:
        yield
    finally:
        sys.version_info = real_version

class ReincarnationFinder(importlib.abc.MetaPathFinder):
    def __init__(self, alias_map):
        self.alias_map = alias_map

    def find_spec(self, fullname, path, target=None):
        if fullname in self.alias_map:
            return self._gen_spec(fullname)
        return None

    def _gen_spec(self, fullname):
        target_name = self.alias_map[fullname]
        origin_spec = importlib.util.find_spec(target_name)
        if origin_spec:
            return origin_spec
        return None


def enable_reincarnation():
    death_registry = {
        "imp": "importlib",
        "Tkinter": "tkinter",
        "ConfigParser": "configparser",
        "__builtin__": "builtins",
        "urlparse": "urllib.parse"
    }

    sys.meta_path.insert(0, ReincarnationFinder(death_registry))


class BytesShadowWrapper:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        attr = getattr(self._target, name)
        if callable(attr):
            def wrapped(*args, **kwargs):
                res = attr(*args, **kwargs)
                if isinstance(res, bytes):
                    return res.decode('utf-8', errors='ignore')
                return res

            return wrapped
        return attr


def shadow_wrap(obj):
    return BytesShadowWrapper(obj)


if __name__ == "__main__":
    enable_reincarnation()

__all__ = (
    'reincarnation',
    'execute_legacy',
    'LegacyTransformer',
    'inject_polyfills',
    'spoof_python_version',
    'contextmanager',
    'imp_polyfill',
    'shadow_wrap',
    'BytesShadowWrapper',
    'ReincarnationFinder',
    'enable_reincarnation'
)