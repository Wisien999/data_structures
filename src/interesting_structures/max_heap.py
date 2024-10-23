from typing import Optional


class MaxHeap:
    def __init__(self, data: Optional[list] = None) -> None:
        if data is None:
            self.data = []
        else:
            self.data = self.build_min_heap(data)
            
    
    @staticmethod
    def _parent(i: int) -> int:
        """Returns index in data array of parent node of given index"""
        if i <= 0:
            return 0
        return (i-1)//2
    
    @staticmethod
    def _left_child(i: int) -> int:
        """Returns index in data array of left child node of given index"""
        return i*2 + 1

    @staticmethod
    def _right_child(i: int) -> int:
        """Returns index in data array of right child node of given index"""
        return i*2 + 2
    

    def insert(self, val: int) -> None:
        """Inserts the given value into the min heap"""
        # print("yo insert", val)
        self.data.append(val)
        i = len(self.data) - 1

        while i > 0 and self.data[i] > self.data[self._parent(i)]:
            # print("loop", i, self._parent(i))
            self.data[i], self.data[self._parent(i)] = self.data[self._parent(i)], self.data[i]
            i = MaxHeap._parent(i)

    def build_min_heap(self, arr: list) -> list:
        """Builds a min heap from values in the given list"""
        heap = []
        
        for el in arr:
            self.insert(el)
        
        return heap
    
    def fix(self, i: int) -> None:
        """Fixes subheap"""
        # Can be done using recursion
        while True:
            lc_i = self._left_child(i)
            rc_i = self._right_child(i)
        
            mini_i = i
            if lc_i < len(self.data) and self.data[lc_i] > self.data[mini_i]:
                mini_i = lc_i
            if rc_i < len(self.data) and self.data[rc_i] > self.data[mini_i]:
                mini_i = rc_i
            
            if mini_i == i:
                break

            self.data[i], self.data[mini_i] = self.data[mini_i], self.data[i]
            i = mini_i
    
    def peek(self) -> int:
        """Returns value of minimal element"""
        if len(self.data) == 0:
            raise IndexError("Heap is empty")

        return self.data[0]
    
    def pop(self) -> int:
        """Returns value of minimal element and removes it from the heap"""
        root_val = self.peek()
        
        last_child_i = len(self.data)-1
        self.data[0], self.data[last_child_i] = self.data[last_child_i], self.data[0]
        self.data.pop()
        
        self.fix(0)
        
        return root_val
    
    def get_size(self) -> int:
        return len(self.data)
        
        
if __name__ == "__main__":
    min_heap = MaxHeap()        
    min_heap.insert(3)
    min_heap.insert(246)
    min_heap.insert(0)
    min_heap.insert(-20)
    min_heap.insert(12)
    print(min_heap.peek())
    print(min_heap.pop())
    print(min_heap.pop())
    print(min_heap.pop())
    print(min_heap.pop())
    print(min_heap.pop())
    print(min_heap.pop())
