"""Binary heap."""

from typing import (
    Protocol, TypeVar,
    Optional,
    Any
)


class Ordered(Protocol):
    """Types that support < comparison."""

    def __lt__(self, other: Any) -> bool:
        """Determine if self is < other."""
        ...


T = TypeVar('T')
Ord = TypeVar('Ord', bound=Ordered)

# Helper functions


def _parent(i: int) -> int:
    """Get the parent index of i."""
    return (i - 1) // 2


def _left(i: int) -> int:
    """Get the left child of i."""
    return 2 * i + 1


def _right(i: int) -> int:
    """Get the right child of i."""
    return 2 * i + 2


def _get_optional(x: list[T], i: int) -> Optional[T]:
    """Get x[i] if i is a valid index, otherwise None."""
    try:
        return x[i]
    except IndexError:
        return None


def _min_child(x: list[Ord], i: int) -> Optional[int]:
    """Get the smallest child of i, if there is any."""
    l, r = _left(i), _right(i)

    # Get values, and handle out-of-bound at the same time
    l_val = _get_optional(x, l)
    if l_val is None:
        return None
    r_val = _get_optional(x, r)
    if r_val is None:
        return l

    # We have two values to pick the smallest from
    return l if l_val < r_val else r


class HeapMixin:
    """
    This class implements the rest of a heap if you implement _fix_down().

    Using @classmethod we get methods we can call on a class rather than
    an object. We don't need a Heap object if we operate on a list, as we
    do in a binary heap, but we need a way to tie up our functions so we
    can insert different solutions to _fix_down, and this is one way to
    do this. You don't need to understand the details, you can just focus
    on the _fix_down() method and implement it below.

    This isn't an approach I would recommend in general, since we are using
    a class where plain functions would be easier to work with, but for this
    application it makes the exercise easier.
    """

    @classmethod
    def _fix_up(cls, x: list[Ord], i: int) -> None:
        """Move the value at x[i] up to its correct location."""
        while i > 0:
            p = _parent(i)
            if not x[i] < x[p]:
                break  # we don't have to move up
            x[i], x[p] = x[p], x[i]
            i = p

    @classmethod
    def _fix_down(cls, _x: list[Ord], _i: int) -> None:
        """Move the value at x[i] down to its correct location."""
        ...

    @classmethod
    def heapify(cls, x: list[Ord]) -> None:
        """Inplace heapify x."""
        for i in reversed(range(len(x))):
            cls._fix_down(x, i)

    @classmethod
    def push(cls, x: list[Ord], val: Ord) -> None:
        """Add val to the heap."""
        x.append(val)
        cls._fix_up(x, len(x) - 1)

    @classmethod
    def pop(cls, x: list[Ord]) -> Ord:
        """Remove the smallest value and return it."""
        val = x[0]
        x[0], x[-1] = x[-1], x[0]
        x.pop()
        cls._fix_down(x, 0)
        return val


class Heap1(HeapMixin):
    """
    Heap with one version of _fix_down().

    This version moves the value down as long as it is
    larger than both its children, swapping it for the
    smaller child.
    """

    @classmethod
    def _fix_down(cls, x: list[Ord], i: int) -> None:
        """Move the value at x[i] down to its correct location."""
        while i < len(x):
            child = _min_child(x, i)
            if child is None or x[i] < x[child]:
                break
            x[i], x[child] = x[child], x[i]
            i = child


class Heap2(HeapMixin):
    """
    Heap with another version of _fix_down().

    This version moves the value all the way down,
    swapping it for the smaller child, and then fix
    it up again to get it to its right location.
    """

    @classmethod
    def _fix_down(cls, x: list[Ord], i: int) -> None:
        """Move the value at x[i] down to its correct location."""
        # FIXME: implement this strategy
        ...
