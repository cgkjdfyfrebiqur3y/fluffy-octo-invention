import functools
@functools.total_ordering
class indexdict(dict):
    def __init__(self, indexes: dict, names: dict):
        super().__init__(names)
        self.indexes = indexes
    def __getitem__(self, keyorindex):
        @functools.singledispatch
        def __getitem__(self, key):
            return super().__getitem__(key)

        @__getitem__.register(int)
        def _(self, index):
            key = self.indexes[index]
            return super().__getitem__(key)
    
    def __setitem__(self, key, value) -> None:
        @functools.singledispatch
        def __setitem__(self,key):
            super(key,value).__setitem__(key,value)
        
        @__setitem__.register(int)
        def _(self,index,value):
            super().__setitem__(self.indexes[index],value)
    
    def __eq__(self, other) -> bool:
        return super().__eq__(other) and self.indexes == other.indexes
    def __lt__(self,_):
        raise TypeError
    

