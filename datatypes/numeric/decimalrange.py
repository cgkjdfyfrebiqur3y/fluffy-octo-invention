from decimal import Decimal
from typing import Union, Iterator

class DecimalRange:
    """A range implementation that works with decimal numbers."""
    
    def __init__(self, start: Union[Decimal, float, str], 
                 stop: Union[Decimal, float, str], 
                 step: Union[Decimal, float, str] = '1'):
        self.start = Decimal(str(start))
        self.stop = Decimal(str(stop))
        self.step = Decimal(str(step))
        
        if self.step == 0:
            raise ValueError("Step cannot be zero")
            
        # Calculate length
        if self.step > 0:
            if self.start > self.stop:
                self._len = 0
            else:
                self._len = int((self.stop - self.start + self.step) / self.step)
        else:
            if self.start < self.stop:
                self._len = 0
            else:
                self._len = int((self.start - self.stop - self.step) / -self.step)
    
    def __iter__(self) -> Iterator[Decimal]:
        value = self.start
        if self.step > 0:
            while value < self.stop:
                yield value
                value += self.step
        else:
            while value > self.stop:
                yield value
                value += self.step
    
    def __len__(self) -> int:
        return self._len
    
    def __getitem__(self, index: int) -> Decimal:
        if 0 <= index < len(self):
            return self.start + self.step * index
        raise IndexError("DecimalRange index out of range")
    
    def __contains__(self, item: Union[Decimal, float, str]) -> bool:
        item = Decimal(str(item))
        if self.step > 0:
            return self.start <= item < self.stop and \
                   (item - self.start) % self.step == 0
        return self.stop < item <= self.start and \
               (self.start - item) % -self.step == 0
    
    def __str__(self) -> str:
        return f"DecimalRange({self.start}, {self.stop}, {self.step})"
    
    def __repr__(self) -> str:
        return str(self)
