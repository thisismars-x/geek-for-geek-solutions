''' lower upper bound here implies you found the item '''
from typing import TypeVar, Sequence, Protocol, Any

class Comparable(Protocol):
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: Any, /) -> bool: ...

T = TypeVar('T', bound = Comparable)

def lower_bound(a: Sequence[T], item: T) -> int :
    ''' Negative index implies, item not found. '''
    n = len(a)
    lo, hi = 0, n

    lb = -1
    while lo <= hi:
        mid = (lo + hi) // 2

        if a[mid] == item: # item found but maybe at a higher index
            lb = mid
            hi = mid - 1
        elif a[mid] > item: hi = mid - 1
        else: lo = mid + 1

    return lb

def upper_bound(a: Sequence[T], item: T) -> int:
    ''' Negative index implies, item not found. '''
    n = len(a)
    lo, hi = 0, n

    ub = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if a[mid] == item:
            ub = mid
            lo = mid + 1
        elif a[mid] > item: hi = mid - 1
        else: lo = mid + 1

    return ub

def insort_left(arr: Sequence[T], item: T) -> int:
    n = len(arr)
    lo, hi = 0, n

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == item: return mid

        if arr[mid] > item: hi = mid - 1
        else: lo = mid + 1

    return lo

def insort_right(arr: Sequence[T], item: T) -> int:
    n = len(arr)
    lo, hi = 0, n

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == item: return mid

        if arr[mid] > item: hi = mid - 1
        else: lo = mid + 1

    return hi
