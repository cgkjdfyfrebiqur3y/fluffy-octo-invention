from typing import TypeVar, Generic, Dict, Iterator



class FrozenDict(dict):
    """An immutable dictionary implementation."""
    
    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
        self._hash = None
    
    def __getitem__(self, key):
        return self._dict[key]
    
    
    
    
    def __iter__(self) -> Iterator:
        return iter(self._dict)
    
    def __len__(self) -> int:
        return len(self._dict)
    
    def __contains__(self, key) -> bool:
        return key in self._dict
    
    def keys(self):
        return self._dict.keys()
    
    def values(self):
        return self._dict.values()
    
    def items(self):
        return self._dict.items()
    
    
    
    def __eq__(self, other):
        if not isinstance(other, FrozenDict):
            return False
        return self._dict == other._dict
    
    def __repr__(self):
        return f"FrozenDict({self._dict})"
