class Flyweight:
    """
    Flyweight parent class to implement Gang of Four flyweight design
    pattern. The flyweight will only create one instance of a given child
    class based on the return of :py:meth:`_key()`. 
    
    :py:meth:`_key()` must be implemented by children. The return of :py:meth:`_key()`
    must be hashable.

    Currently, children must define class variable :py:attr:`_instances`. This is to
    create special "namespaces" for instances to be tied to individual classes
    and not the :class:`Flyweight` parent class itself.
    """
    __slots__ = []

    def __new__(cls, *args, **kwargs):
        key = cls._key(cls, *args, **kwargs)
        return cls._instances.setdefault(key, super(type(cls), cls).__new__(cls))

    @classmethod
    def has_key(cls, *args):
        key = args if len(args) > 1 else args[0]
        return key in cls._instances.keys()

    @classmethod
    def from_key(cls, *args):
        key = args if len(args) > 1 else args[0]
        return cls._instances.get(key, None)

    def _key(cls, *args, **kwargs):
        # return (args, tuple(kargs.items()))
        raise NotImplementedError
