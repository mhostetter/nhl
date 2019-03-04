def select(item, attr, default=None):
    if len(attr.split(".")) > 1:
        next_item = getattr(item, attr.split(".")[0], default)
        next_attr = attr.split(".")[1]
        return select(next_item, next_attr, default)
    else:
        return getattr(item, attr, default)

class List(list):
    """
    Searchable, sortable, and filter-able list subclass
    """
    def select(self, attr):
        return List([select(item, attr, None) for item in self])
