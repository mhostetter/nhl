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
        key = cls._key(*args, **kwargs)
        return cls._instances.setdefault(key, super(type(cls), cls).__new__(cls))

    def _key(cls, *args, **kwargs):
        """
        Obtain objects keys from the construction arguments. Called by `__new__()`.

        Returns:
            int or tuple: Object key
        """
        raise NotImplementedError

    @classmethod
    def keys(cls):
        """
        Obtains the current flyweight keys for the given class.

        Returns:
            dict_keys: All keys for class `cls` currently created
        """
        return cls._instances.keys()

    @classmethod
    def has_key(cls, *args):
        """
        Check whether flyweight object with specified key has already been created.

        Returns:
            bool: True if already created, False if not
        """
        key = args if len(args) > 1 else args[0]
        return key in cls._instances.keys()

    @classmethod
    def from_key(cls, *args):
        """
        Return flyweight object with specified key, if it has already been created.

        Returns:
            cls or None: Previously constructed flyweight object with given
            key or None if key not found
        """
        key = args if len(args) > 1 else args[0]
        return cls._instances.get(key, None)
