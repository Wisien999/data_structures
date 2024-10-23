# Proszę przedstawić W jaki sposób zrealizować strukturę danych, która pozwala wykonywać
# operacje:
# 1. Insert
# 2. RemoveMedian (wyciągnięcie mediany)
# tak, żeby wszystkie operacje działały w czasie O(log n).


# Mamy dwa kopce. Jeden min-heap i jeden max-heap. W max heapie-przymamy elementy mniejsze. w min-heapie trzymame elementy większe 
# Wstawianie odbywa się następująco:
# Wstawiany element jest większy od korzenia w min-heapie -> (należy do elementów większych) -> wstaw go do min-heap'u
# wstawiany element jes mniejszy od korzenia w max-heapie -> (należy do elementów mniejszych) -> wstaw go do max-heap'u
# w pozostałych przypadkach -> wstaw go gdziekolwiek
# jeżeli w którymś z kopców są przynajmniej 2 elementy więcej niż w drugim to przenieś korzeń z większego kopca do mnieszego

# removeMedian:
# jeżeli kopce są różnej wielkości -> usuń i zwróć korzeń kopca większego
# w przeciwnym wypadku -> usuń i zwróć korzenie obu kopców

from typing import Iterable, Optional, Tuple
from min_heap import MinHeap
from max_heap import MaxHeap



class FastMedian:
    def __init__(self, array: Optional[list] = None) -> None:
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
        
        if array:
            self.build(array)
    
    def insert(self, val: int) -> None:
        if self.min_heap.get_size() == 0 or val > self.min_heap.peek():
            self.min_heap.insert(val)
        else:
            self.max_heap.insert(val)
        

        while self.max_heap.get_size() - self.min_heap.get_size() >= 2:
            tmp = self.max_heap.pop()
            self.min_heap.insert(tmp)

        while self.min_heap.get_size() - self.max_heap.get_size() >= 2:
            tmp = self.min_heap.pop()
            self.max_heap.insert(tmp)


    def remove_median(self) -> float:
        if self.min_heap.get_size() > self.max_heap.get_size():
            return self.min_heap.pop()
        if self.min_heap.get_size() < self.max_heap.get_size():
            return self.max_heap.pop()
        
        # this return value depends on definition of median for even array length
        return (self.max_heap.pop() + self.min_heap.pop())/2
        # return self.max_heap.pop(), self.min_heap.pop()
    
    def build(self, arr: list) -> None:
        self.min_heap.data.clear()
        self.max_heap.data.clear()
        
        for el in arr:
            self.insert(el)


if __name__ == "__main__":
    arr = [63234,53,6,3,3,4,424,2,5,34645,7,56,734,5,23,42]
    print(len(arr))
    print(sorted(arr))
    fm = FastMedian()
    fm.build(arr)
    print(fm.remove_median())
