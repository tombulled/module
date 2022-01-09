import sys
import types
import typing

def override(obj: typing.Any, /, *, module: typing.Optional[typing.Union[str, types.ModuleType]] = None):
    if module is None:
        module = obj.__module__
    elif isinstance(module, types.ModuleType):
        module = module.__module__

    sys.modules[module] = obj