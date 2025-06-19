from math import sqrt, atan2, cos, sin, pi
from typing import Union, SupportsFloat

class Complex:
    """A complex number implementation."""
    
    def __init__(self, real: float = 0, imag: float = 0):
        self.real = float(real)
        self.imag = float(imag)
    
    @classmethod
    def from_polar(cls, r: float, theta: float) -> 'Complex':
        """Create a complex number from polar coordinates."""
        return cls(r * cos(theta), r * sin(theta))
    
    def __add__(self, other: Union['Complex', SupportsFloat]) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return Complex(self.real + float(other), self.imag)
    
    def __sub__(self, other: Union['Complex', SupportsFloat]) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return Complex(self.real - float(other), self.imag)
    
    def __mul__(self, other: Union['Complex', SupportsFloat]) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real
            )
        other = float(other)
        return Complex(self.real * other, self.imag * other)
    
    def __truediv__(self, other: Union['Complex', SupportsFloat]) -> 'Complex':
        if isinstance(other, Complex):
            denom = other.real ** 2 + other.imag ** 2
            return Complex(
                (self.real * other.real + self.imag * other.imag) / denom,
                (self.imag * other.real - self.real * other.imag) / denom
            )
        other = float(other)
        return Complex(self.real / other, self.imag / other)
    
    def conjugate(self) -> 'Complex':
        """Return the complex conjugate."""
        return Complex(self.real, -self.imag)
    
    def __abs__(self) -> float:
        """Return the magnitude."""
        return sqrt(self.real ** 2 + self.imag ** 2)
    
    def arg(self) -> float:
        """Return the argument (angle) in radians."""
        return atan2(self.imag, self.real)
    
    def __repr__(self) -> str:
        if self.imag == 0:
            return f"{self.real}"
        elif self.real == 0:
            return f"{self.imag}j"
        else:
            return f"({self.real} + {self.imag}j)"
