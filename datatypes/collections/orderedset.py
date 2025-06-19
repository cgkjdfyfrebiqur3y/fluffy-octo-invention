class OrderedSet:
    """An ordered set implementation that maintains insertion order."""
    
    def __init__(self, iterable=None):
        self._items = dict()
        if iterable is not None:
            self.update(iterable)
    
    def add(self, item):
        """Add an item to the set."""
        self._items[item] = None
    
    def discard(self, item):
        """Remove an item from the set if it exists."""
        self._items.pop(item, None)
    
    def remove(self, item):
        """Remove an item from the set, raising KeyError if not found."""
        del self._items[item]
    
    def update(self, iterable):
        """Update the set with items from an iterable."""
        for item in iterable:
            self.add(item)
    
    def __iter__(self):
        return iter(self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __repr__(self):
        return f"OrderedSet({list(self)})"
