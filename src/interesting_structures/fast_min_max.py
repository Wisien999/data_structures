# Proszę zaprojektowac strukturę danych przechowującą liczby i pozwalającą na następujące
# operacje (zakładamy, że wszystkie liczby umieszczane w strukturze są różne):
# Init(n). Tworzy zadaną strukturę danych zdolną pomieścić maksymalnie n liczb.
# Insert(x). Dodaje do struktury liczbę x.
# RemoveMin() Znajduje najmniejszą liczbę w strukturze, usuwa ją i zwraca jej wartość.
# RemoveMax() Znajduje największą liczbę w strukturze, usuwa ją i zwraca jej wartość.
# Każda z operacji powinna mieć złożoność O(log n), gdzie n to ilość liczb znajdujących się obecnie
# w strukturze. W tym zadaniu nie trzeba implementować podanych operacji, a jedynie
# przekonująco opisać jak powinny być zrealizowane i dlaczego mają wymaganą złożoność.


# Heap based structure that allows fast element adding and removing maximal/minmal element.
# n - ammount of elements in structure
# Available functions and their time complexities
# insert(x) - adds x to the structure O(log(n))
# pop_min() -> Any


class Fast_min_max:
    def __init__(self) -> None:
        self.min_heap = []
        self.max_heap = []
        self.size = 0

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


    def _swap_min(self, i, j):
        self.max_heap[self.min_heap[i][1]][1] = j
        self.max_heap[self.min_heap[j][1]][1] = i
        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]
        
    def _swap_max(self, i, j):
        self.min_heap[self.max_heap[i][1]][1] = j
        self.min_heap[self.max_heap[j][1]][1] = i
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]


    def insert(self, x):
        min_el = [x, self.size]
        max_el = [x, self.size]
        self.min_heap.append(min_el)
        self.max_heap.append(max_el)

        # Insert to min heap
        min_i = self.size
        while min_i > 0 and self.min_heap[min_i][0] < self.min_heap[Fast_min_max._parent(min_i)][0]:
            parent_i = Fast_min_max._parent(min_i)
            self._swap_min(min_i, parent_i)
            min_i = parent_i

        # Insert to max heap
        max_i = self.size
        while max_i > 0 and self.max_heap[max_i][0] > self.max_heap[Fast_min_max._parent(max_i)][0]:
            parent_i = Fast_min_max._parent(max_i)
            self._swap_max(max_i, parent_i)
            max_i = parent_i
        
        self.size += 1
        
        return min_i, max_i
    

    def fix_min(self, i: int) -> None:
        """Fixes subheap"""
        # Can be done using recursion
        while True:
            lc_i = Fast_min_max._left_child(i)
            rc_i = Fast_min_max._right_child(i)
        
            mini_i = i
            if lc_i < self.size and self.min_heap[lc_i][0] < self.min_heap[mini_i][0]:
                mini_i = lc_i
            if rc_i < self.size and self.min_heap[rc_i][0] < self.min_heap[mini_i][0]:
                mini_i = rc_i
            
            if mini_i == i:
                break

            self._swap_min(i, mini_i)
            i = mini_i

    def fix_max(self, i: int) -> None:
        """Fixes subheap"""
        # Can be done using recursion
        while True:
            lc_i = Fast_min_max._left_child(i)
            rc_i = Fast_min_max._right_child(i)
        
            maxi_i = i
            if lc_i < self.size and self.max_heap[lc_i][0] > self.max_heap[maxi_i][0]:
                maxi_i = lc_i
            if rc_i < self.size and self.max_heap[rc_i][0] > self.max_heap[maxi_i][0]:
                maxi_i = rc_i
            
            if maxi_i == i:
                break

            self._swap_max(i, maxi_i)
            i = maxi_i


    def pop_min(self):
        """Removes the minimum element and returns its value"""

        if self.size == 0:
            raise KeyError("Structure is empty")

        self.size -= 1
        
        n = self.size
        self._swap_min(0, n)
        val = self.min_heap[-1]
        self._swap_max(val[1], n)
        self.fix_max(val[1])
        self.fix_min(0)
        
        self.max_heap.pop()
        self.min_heap.pop()

        return val[0]

    def pop_max(self):
        """Removes the maximum element and returns its value"""

        if self.size == 0:
            raise KeyError("Structure is empty")

        self.size -= 1
        
        n = self.size
        self._swap_max(0, n)
        val = self.max_heap[-1]
        self._swap_min(val[1], n)
        self.fix_min(val[1])
        self.fix_max(0)
        
        self.min_heap.pop()
        self.max_heap.pop()

        return val[0]



if __name__ == "__main__":
    min_max = Fast_min_max()
    min_max.insert(3)
    min_max.insert(7)
    min_max.insert(9)
    min_max.insert(4)
    min_max.insert(14)
    min_max.insert(8)
    print(min_max.min_heap)
    print(min_max.max_heap)
    print(min_max.pop_min())
    print(min_max.min_heap)
    print(min_max.max_heap)
    print(min_max.pop_min())
    print(min_max.min_heap)
    print(min_max.max_heap)
    print(min_max.pop_max())
    print(min_max.min_heap)
    print(min_max.max_heap)
    
