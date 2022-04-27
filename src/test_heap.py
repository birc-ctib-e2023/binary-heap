"""Testing binary heaps."""

from heap import HeapMixin, Heap1, Heap2
from typing import Type


def sort_with_heap(x: list[int], heap: Type[HeapMixin]) -> list[int]:
    """Sort x using a heap class."""
    x = x[:]  # work on a copy
    heap.heapify(x)
    res = []
    while x:
        res.append(heap.pop(x))
    return res


def test_heaps() -> None:
    """Rudementary test of heaps."""
    x = [5, 2, 4, 1, 3, 1, 5, 6, 7]
    heap_sorted = sort_with_heap(x, Heap1)
    assert list(sorted(x)) == heap_sorted

    heap_sorted = sort_with_heap(x, Heap2)
    assert list(sorted(x)) == heap_sorted
