import sys
import types
import typing

def call(func: typing.Callable, /, *, module: typing.Optional[typing.Union[str, types.ModuleType]] = None):
    if module is None:
        module = func.__module__
    elif isinstance(module, types.ModuleType):
        module = module.__module__

    class CallableModule(types.ModuleType):
        __call__ = staticmethod(func)

    module: types.ModuleType = \
    (
        module
        if isinstance(module, types.ModuleType)
        else sys.modules[module]
    )

    module.__class__: typing.Type[CallableModule] = CallableModule