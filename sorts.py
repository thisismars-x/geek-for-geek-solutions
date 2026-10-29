from typing import Protocol, TypeVar, Any

class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...

T = TypeVar('T', bound = Comparable)

def Max_Heapify(A: list[T], index: int, heap_size: int):
    left, right = (index << 1) + 1, (index << 1) + 2

    largest = index
    if left < heap_size and A[left] > A[index]: largest = left
    if right < heap_size and A[right] > A[largest]: largest = right

    if largest != index:
        A[largest], A[index] = A[index], A[largest]
        Max_Heapify(A, largest, heap_size)

def Build_Max_Heap(A: list[T]): 
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        Max_Heapify(A, i, n)

def Heap_Sort(A: list[T]):
    n = len(A)
    heap_size = n

    Build_Max_Heap(A)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        Max_Heapify(A, 0, heap_size)

def Insertion_Sort(A: list[int]):
    n = len(A)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j] < A[j - 1]: A[j], A[j-1] = A[j-1], A[j]
            else: break

import sys

class Priority_Queue:

    def __init__(self, data: list[T]):
        self.data = data.copy()
        Build_Max_Heap(self.data)

    def increase_key(self, i: int, key: T):
        if key < self.data[i]:
            raise RuntimeError(
                f"Called increase_key with a key less than data = {self.data[i]}"
            )

        self.data[i] = key

        while i > 0:
            parent = (i - 1) // 2

            if self.data[parent] >= self.data[i]:
                break

            self.data[parent], self.data[i] = (
                self.data[i],
                self.data[parent]
            )

            i = parent

    def insert(self, key: T):
        self.data.append(-sys.maxsize)
        self.increase_key(len(self.data) - 1, key)

    def __str__(self):
        return f"Priority_Queue({self.data})"
a = Priority_Queue([1, 2, 3, 6, 4, 2])
a.insert(100)
print(a)

