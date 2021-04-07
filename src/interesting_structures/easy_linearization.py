from typing import Any, Iterator
from collections.abc import Sequence
import math


class Linear_2D_array(Sequence):
    """
    Abstraction layer that allows using 2D array of size NxN like 1D array of size N^2.
    Input array is mapped to areas A, B and C like this:
    +-------------+
    | B1 C6 C5 C3 |
    | A1 B2 C4 C2 |
    | A2 A3 B3 C1 |
    | A4 A5 A6 B4 |
    +-------------+
    is mapped to
    [A1...A6|B1...B4|C1...C6]
    """

    def __init__(self, array) -> None:
        self.array = array
        self.size = len(array)

        
    @staticmethod
    def get_index_groupA(i: int) -> tuple[int, int]:
        """
        Converts i index in a flat array to x and y in 2D quadratic array (only in group A)
        """

        # solve 1+2+3+...+y >= i+1 for the smallest natural y
        # in rows 1, 2, 3, ..., y is enough cells for i-th smallest elelent to fit in
        y = math.ceil((math.sqrt(9+8*i)-1)/2)

        if y*(y-1)//2 >= i+1: # (never gonna happen (I think so, at least))
            print("reduced")
            y -= 1

        earlier = y*(y-1) // 2 # How many cells are earlier
        x = i - earlier
        
        return x, y
    
    def get_index(self, i: int) -> tuple[int, int]:
        AC_areas_len = (self.size**2 - self.size) // 2
        if i >= AC_areas_len and i < AC_areas_len + self.size:
            idx = i - AC_areas_len
            return idx, idx

        if i < AC_areas_len:
            return Linear_2D_array.get_index_groupA(i)
        
        # weird hack
        y, x = Linear_2D_array.get_index_groupA(self.size**2 - i - 1)
        return x, y
        
    
    def __len__(self) -> int:
        return self.size**2

    def __getitem__(self, i: int) -> Any:
        x, y = self.get_index(i)
        return self.array[y][x]
    
    def __setitem__(self, i: int, val: Any) -> None:
        x, y = self.get_index(i)
        self.array[y][x] = val
    
    def __iter__(self) -> Iterator:
        self.i = 0
        return self

    def __next__(self) -> Any:
        if self.i >= self.size**2:
            raise StopIteration
        
        val = self[self.i]
        self.i += 1
        return val
    
    def __str__(self) -> str:
        return str([self[i] for i in range(len(self))])







if __name__ == "__main__":
    arr = [
        [6, 15, 14, 12],
        [0, 7,  13, 11],
        [1, 2,  8,  10],
        [3, 4,  5,  9]
    ]

    test = Linear_2D_array(arr)
    print(test)
    for el in arr:
        print(el, end=" ")
    print()
    for i in range(len(test)):
        print(test[i], end=" ")
    print("after i")
    for el in test:
        print(el, end=" ")
    print()