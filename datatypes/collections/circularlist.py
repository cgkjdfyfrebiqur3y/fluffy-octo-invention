from collections.abc import Sequence
from itertools import cycle
class CircularListIterator():
    """An iterator for a CircularList"""
    def __init__(self,circularlist,skipitems=0) -> None:
        self.circularlist = circularlist
        self.__iterator = cycle(self.circularlist)
        self.__items_skipped = skipitems
        for _ in range(skipitems):
            self.__iterator.__next__()
    def __next__(self):
        self.__items_skipped += 1
        return next(self.__iterator)
    def __str__(self) -> str:
        realvalue = f"""
        Circular list iterator for {self.circularlist}.
        """
        return realvalue
    def __repr__(self):
        return f"CircularListIterator({self.circularlist},{self.__items_skipped})"
    

class CircularList():
    """A list implementation that wraps around at boundaries."""
    
    def __init__(self, items:Sequence):
        self._items = list(items) if items is not None else []
    
    def __getitem__(self, index: int):
        if not self._items:
            raise IndexError("CircularList is empty")
        return self._items[index % len(self)]
    
    def __setitem__(self, index: int, value) -> None:
        if not isinstance(index,int):
            raise CircularListIndexError
        if not self._items:
            raise IndexError("CircularList is empty")
        self._items[index % len(self)] = value
    
    def append(self, item) -> None:
        """Add an item to the end of the list."""
        self._items.append(item)
    
    def pop(self, index: int = -1):
        """Remove and return item at index."""
        if not self._items:
            raise IndexError("CircularList is empty")
        return self._items.pop(index % len(self))
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self) -> CircularListIterator:
        return CircularListIterator(self._items)
    
    def rotate(self, steps: int = 1) -> None:
        """Rotate the list by a number of steps."""
        if not self._items:
            return
        steps = steps % len(self)
        self._items = self._items[steps:] + self._items[:steps]
    
    def __repr__(self) -> str:
        return f"CircularList({self._items})"
