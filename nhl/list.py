def _select(item, attr, default=None):
    if len(attr.split(".")) > 1:
        next_item = getattr(item, attr.split(".")[0], default)
        next_attr = attr.split(".")[1]
        return _select(next_item, next_attr, default)
    else:
        return getattr(item, attr, default)

class List(list):
    """
    Searchable, sortable, and filter-able :class:`list` subclass
    """
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
