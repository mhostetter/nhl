import builtins

SPHINX_BUILD = hasattr(builtins, "__sphinx_build__")


def set_module(module):
    """
    A decorator to update the __module__ variable.
    """
    def decorator(obj):
        if not SPHINX_BUILD:
            # Sphinx gets confused when parsing overloaded functions when the module is modified using this decorator.
            # We set the __sphinx_build__ variable in conf.py and avoid modifying the module when building the docs.
            if module is not None:
                obj.__module__ = module

        return obj

    return decorator
