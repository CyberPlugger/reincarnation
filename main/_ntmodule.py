import sys
import importlib
import inspect
import os

def __getattr__(name):
    """Dynamic import hook: reincarnation.module.any_module"""
    if name in sys.modules:
        return sys.modules[name]
    try:
        return importlib.import_module(name)
    except ImportError:
        raise AttributeError(f"Module '{name}' is not reachable via Reincarnation.")

def where(module_name):
    """Find the physical path of a module"""
    try:
        mod = importlib.import_module(module_name) if isinstance(module_name, str) else module_name
        return os.path.abspath(mod.__file__)
    except Exception:
        return "Unknown or Built-in"

def reload(module_obj):
    """Force reincarnation: Reload an existing module"""
    return importlib.reload(module_obj)

def source(obj):
    """Extract the DNA: Get source code of any function or class"""
    try:
        return inspect.getsource(obj)
    except Exception as e:
        return f"Could not extract source: {e}"

def hijack(target_module_name, func_name, new_func):
    """Function Transplant: Replace a function in another module"""
    mod = importlib.import_module(target_module_name) if isinstance(target_module_name, str) else target_module_name
    original = getattr(mod, func_name)
    setattr(mod, func_name, new_func)
    return original # Return original to allow restoration later

def steal(from_module, to_module, attr_name):
    """Attribute Theft: Move a function/class from one module to another"""
    src = importlib.import_module(from_module) if isinstance(from_module, str) else from_module
    dst = importlib.import_module(to_module) if isinstance(to_module, str) else to_module
    setattr(dst, attr_name, getattr(src, attr_name))

def peek(module_name):
    """X-Ray Vision: List all members of a module without importing manually"""
    mod = importlib.import_module(module_name) if isinstance(module_name, str) else module_name
    return [item for item in dir(mod) if not item.startswith('__')]

def teleport(path):
    """Add a new dimension: Inject a path into sys.path for instant access"""
    if path not in sys.path:
        sys.path.insert(0, path)

def exists(module_name):
    """Ghost Scanner: Check if a module can be found without loading it"""
    return importlib.util.find_spec(module_name) is not None
