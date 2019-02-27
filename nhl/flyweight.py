class Flyweight:
    """
    Flyweight parent class to implement Gang of Four flyweight design
    pattern. The flyweight will only create one instance of a given child
    class based on the return of `_key()`. `_key()` must be implemented
    by any children. The return of `_key()` must be hashable.
    """
    __slots__ = []
    __instances = {}

    def __new__(cls, *args, **kwargs):
        key = cls._key(cls, *args, **kwargs)
        return cls.__instances.setdefault(key, super(type(cls), cls).__new__(cls))

    def _key(cls, *args, **kwargs):
        # return (args, tuple(kargs.items()))
        raise NotImplementedError
