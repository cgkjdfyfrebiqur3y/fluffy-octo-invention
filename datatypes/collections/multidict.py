from typing import Any, List, TypeVar, Generic

KT = TypeVar('KT')
VT = TypeVar('VT')

class MultiDict(Generic[KT, VT]):
    """A dictionary that can store multiple values for each key."""
    
    def __init__(self):
        self._items = {}
    
    def add(self, key: KT, value: VT) -> None:
        """Add a value to a key."""
        if key not in self._items:
            self._items[key] = []
        self._items[key].append(value)
    
    def get(self, key: KT) -> List[VT]:
        """Get all values for a key."""
        return self._items.get(key, [])
    
    def get_one(self, key: KT) -> VT:
        """Get the first value for a key."""
        values = self.get(key)
        if not values:
            raise KeyError(key)
        return values[0]
    
    def remove(self, key: KT, value: VT = None) -> None:
        """Remove a specific value for a key, or all values if value is None."""
        if value is None:
            self._items.pop(key, None)
        else:
            if key in self._items:
                self._items[key] = [v for v in self._items[key] if v != value]
                if not self._items[key]:
                    del self._items[key]
    
    def items(self):
        """Return all key-value pairs."""
        for key, values in self._items.items():
            for value in values:
                yield key, value
    
    def __len__(self) -> int:
        return sum(len(values) for values in self._items.values())
    
    def __str__(self) -> str:
        return str(dict(self.items()))
