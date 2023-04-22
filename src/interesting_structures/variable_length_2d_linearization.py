from typing import MutableSequence, TypeVar
from intervaltree import IntervalTree, Interval

T = TypeVar("T", bound=MutableSequence)


class LineListLinearizer(MutableSequence):
    '''
    This structure can be used to linearize array of arrays where inner arrays does not have to be of the same length.

    It was developed as an util for another project so it is very lacking and only a few besic operations were implemented.
    '''
    def __init__(self, array_of_arrays: list[list[int]]) -> None:
        index_intervals = []
        idx = 0
        for array in array_of_arrays:
            index_intervals.append(Interval(idx, idx + len(array), data=array))
            idx += len(array)

        self.tree = IntervalTree(index_intervals)

    def __getitem__(self, i: int) -> int:
        interval = self.tree.at(i).pop()
        array: list[int] = interval.data

        return array[i - interval.begin]

    def __setitem__(self, i: int, val: int) -> None:
        # assumes i is already in the existing range
        interval = self.tree.at(i).pop()
        line: list[int] = interval.data
        line[i - interval.begin] = val

    def __delitem__(self, i: int) -> None:
        raise NotImplementedError()

    def insert(self, index: int, value: int) -> None:
        raise NotImplementedError()

    def __len__(self) -> int:
        return self.tree.end() - self.tree.begin()

    def get_unlinearized(self) -> list[list[int]]:
        return [interval.data for interval in self.tree.items()]
