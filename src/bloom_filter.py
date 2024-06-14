from dataclasses import dataclass
from typing import TypeVar, Callable, Iterable, MutableSequence
import math
import numpy as np

T = TypeVar("T")

@dataclass
class BloomFilter[T]:
    mem: MutableSequence[int]
    calc_hashes: Callable[[T], Iterable[int]]

    @staticmethod
    def false_pos_rate(hashes:int, m_size:int, items:int):
        return (1.0-math.exp(-hashes*items/m_size))**hashes

    def add(self, item:T):
        for h in self.calc_hashes(item):
            self.mem[h%len(self.mem)]=1
    
    def __contains__(self, item:T):
        return all(self.mem[h%len(self.mem)] for h in self.calc_hashes(item))
    
@dataclass
class BitArray:
    data: np.array[int]
    size: int

    @classmethod
    def zeros(cls, n:int):
        a_size, rem = divmod(n, 8)
        if rem:
            a_size+=1
        data = np.asarray('B', (0 for _ in range(a_size)))
        return cls(data=data, size=n)
    
    def __getitem__(self, n:int):
        a_idx, b_idx = divmod(n, 8)
        return (self.data[a_idx] >> b_idx) & 0b1
    
    def __setitem__(self, n:int, bit:int):
        a_idx, b_idx = divmod(n, 8)
        data = self.data[a_idx]
        data &= ~(1 << b_idx)
        data |= (bool(bit)*(1 << b_idx))
        self.data[a_idx] = data

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"