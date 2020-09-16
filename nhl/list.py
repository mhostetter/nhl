import operator

OPERATIONS = {
    "==": operator.eq,
    "=": operator.eq,
    "eq": operator.eq,
    "!=": operator.ne,
    "ne": operator.ne,
    ">": operator.gt,
    "gt": operator.gt,
    ">=": operator.ge,
    "ge": operator.ge,
    "<": operator.lt,
    "lt": operator.lt,
    "<=": operator.le,
    "le": operator.le,
    "in": operator.contains,
    "contains": operator.contains
}


def _select(item, attr, default=None):
    if len(attr.split(".")) > 1:
        next_item = getattr(item, attr.split(".")[0], default)
        next_attr = attr.split(".")[1]
        return _select(next_item, next_attr, default)
    else:
        return getattr(item, attr, default)


def _filter(item, comparent, compare="=="):
    compare = compare.strip()
    if isinstance(comparent, str):
        compare = "in"
        item = item.lower()
        comparent = comparent.lower()
    operation = OPERATIONS[compare]
    return operation(item, comparent)


class List(list):
    """
    Searchable, sortable, and filter-able :class:`list` subclass
    """

    def __add__(self, other):
        return List(super().__add__(other))

    def unique(self):
        """
        Reduce the list to unique elements.

        Returns:
            nhl.List: reduced list
        """
        return List(set(self))

    def select(self, attr, default=None):
        """
        Select a given attribute (or chain or attributes) from the objects within the
        list.

        Args:
            attr (str): attributes to be selected (with initial `.` omitted)
            default (any): value to return if given element in list doesn't contain
                desired attribute

        Returns:
            nhl.List: list of selected attribute values
        """
        return List([_select(item, attr, default) for item in self])

    def filter(self, attr, value, compare="=="):
        """
        Filter list by a comparison of a given attribute (or chain or attributes).

        Args:
            attr (str): attributes to be compared (with initial `.` omitted)
            value (any): value to compare attr against
            compare (str): comparison type
                "==", "=", "eq": `attr == value`
                "!=", "ne": `attr != value`
                ">", "gt": `attr > value`
                ">=", "ge": `attr >= value`
                "<", "lt": `attr < value`
                "<=", "le": `attr <= value`
                "in", "contains": `value in attr`

        Returns:
            nhl.List: reduced list with items that satisfy filter criterion
        """
        return List([item for item in self if _filter(_select(item, attr), value, compare)])

    def sort(self, key, reverse=False):
        """
        Sort the list by `key` either ascending or descending.

        Args:
            key (str): atrribute to sort by (with initial `.` omitted)
            reverse (bool, optional): reverse the direction of sort to descending, (default False, ascending)

        Returns:
            nhl.List: sorted list
        """
        return List(sorted(self, key=lambda item: _select(item, key), reverse=reverse))

    @property
    def len(self):
        """
        Helper property to return length of list

        Returns:
            int: length of list `len(self)`
        """
        return len(self)
