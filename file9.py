# linked list
#

from __future__ import annotations
from typing import Any, Sequence

class Singly_Linked_List:
    def __init__(self, data: Any, next: Singly_Linked_List | None = None): self.data, self.next = data, next

    def insert(self, data: Any):
        tmp_node = Singly_Linked_List(self.data, self.next)
        self.data, self.next = data, tmp_node

    def reverse(self) -> Singly_Linked_List:
        tmp_node = self
        ll = Singly_Linked_List(tmp_node.data)
        tmp_node = tmp_node.next

        while tmp_node:
            ll.insert(tmp_node.data)
            tmp_node = tmp_node.next

        return ll

    def swap(self, i: int, j: int):
        ''' Swap the data in index i and j. '''
        tmp_node_i, tmp_node_j = None, None

        tmp_node = self
        count = 0

        while tmp_node:
            if i == count: tmp_node_i = tmp_node
            if j == count: tmp_node_j = tmp_node
            tmp_node = tmp_node.next
            count += 1

        if not tmp_node_i or not tmp_node_j: raise ValueError(f"Can not swap index i = {i}, j = {j}, for a singly linked list of size = {count}.")
        assert isinstance(tmp_node_i, Singly_Linked_List) and isinstance(tmp_node_j, Singly_Linked_List), "Impossible condition"
        tmp_node_i.data, tmp_node_j.data = tmp_node_j.data, tmp_node_i.data

    @classmethod
    def make(cls, anything: Sequence) -> Singly_Linked_List:
        assert len(anything) > 0, "Can not make a LinkedList with an empty iterable"
        ll = cls(anything[0])
        for stuff in anything[1:]: ll.insert(stuff)
        return ll

    def __repr__(self) -> str:
        fmt = f"{self.__class__.__name__}("

        tmp_node = self
        while tmp_node:
            fmt += f"{tmp_node.data}, "
            tmp_node = tmp_node.next

        fmt += ")"

        return fmt


class Doubly_Linked_List:
    def __init__(self, data: Any, next: Doubly_Linked_List | None = None, prev: Doubly_Linked_List | None = None): self.data, self.next, self.prev = data, next, prev

    def insert(self, data: Any):
        tmp_node = Doubly_Linked_List(self.data, self.next)
        self.data, self.next, self.prev = data, tmp_node, None

    @classmethod
    def make(cls, anything: Sequence) -> Doubly_Linked_List:
        assert len(anything) > 0, "Can not make a doubly linked list with input iterable of size 0"
        dll = cls(anything[0])
        for stuff in anything[1:]: dll.insert(stuff)
        return dll

    def reverse(self) -> Doubly_Linked_List:
        tmp_node = self
        dll = Doubly_Linked_List(tmp_node.data)
        tmp_node = tmp_node.next

        while tmp_node:
            dll.insert(tmp_node.data)
            tmp_node = tmp_node.next

        return dll

    def __repr__(self) -> str:
        fmt = f"{self.__class__.__name__}("

        tmp_node = self
        while tmp_node:
            fmt += f"{tmp_node.data}, "
            tmp_node = tmp_node.next

        fmt += ")"
        return fmt

def Reverse_In_Groups_Of_Size_K(sll: Singly_Linked_List, k: int) -> Singly_Linked_List:

    # first of all find out the length of the list
    #
    len_sll = 0
    tmp_node = sll

    while tmp_node:
        len_sll += 1
        tmp_node = tmp_node.next

    # reverse in windows
    #
    remaining_ll = len_sll
    start = 0

    this_chunk_size = k
    while remaining_ll > 0:
        if remaining_ll < k:
           this_chunk_size = remaining_ll

        # lo, hi = start, start + this_chunk_size - 1
        # while lo < hi:
        #     sll.swap(lo, hi)
        #     lo += 1
        #     hi -= 1

        # same as above, only shorter
        for i in range(this_chunk_size // 2): sll.swap(start + i, start + this_chunk_size - 1 - i)

        start += this_chunk_size
        remaining_ll -= this_chunk_size

    return sll
