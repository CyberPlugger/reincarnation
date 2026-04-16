import sys
import types

class TrickPython:
    def local_import_save(self, module, modern_shims=None):
        vessel = types.ModuleType(module)
        sys.modules[vessel.__name__] = vessel

        if modern_shims:
            for attr_name, modern_func in modern_shims.items():
                setattr(vessel, attr_name, modern_func)

        return vessel