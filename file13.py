from __future__ import annotations
from ast import Add
from tarfile import LNKTYPE
from typing import cast

class ListNode:
    def __init__(self, val: int, next: None | ListNode = None):
        self.val, self.next = val, next

    def __repr__(self) -> str:
        f = "ListNode(val=["

        tmp = self
        while tmp:
            f += f"{tmp.val}"
            tmp = tmp.next
            if tmp: f += ", "

        f += "])"
        return f


a = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

def Middle_Linked_List(head: ListNode) -> int:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


def Remove_Nth(head: ListNode, k: int) -> ListNode:

    # # looks like we need at least 2 O(n) operations
    # length = 0
    # tmp = head
    # while tmp:
    #     length += 1
    #     tmp = tmp.next

    # prior_node = head
    # if k == length: head = head.next
    # elif k > length: raise RuntimeError(f"Asked to delete k:{k}th element with linked list of size:{length}")
    # else:
    #     for _ in range(length - k - 1):
    #         prior_node = prior_node.next

    # prior_node.next = prior_node.next.next
    # return head

    # optimal approaach
    #
    fast, slow = head, head
    for _ in range(k):
        # if not fast: return head
        fast = fast.next

    if not fast:
        head = head.next
        return head

    while fast and fast.next:
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next
    return head

def Palindrome(head: ListNode) -> bool:

    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        if fast: slow = slow.next

    head2 = slow.next
    slow.next = None # breaking the list this requires later repair

    # reverse head2
    #
    curr, prev = head2, None

    while curr:
        after_curr = curr.next
        curr.next = prev
        curr, prev = after_curr, curr

    head2 = prev

    ptr1, ptr2 = head, head2
    pal = True
    while ptr1 and ptr2:
        if not pal: break
        if ptr1.val != ptr2.val:
            pal = False

        ptr1 = ptr1.next
        ptr2 = ptr2.next


    # restore original list
    #
    curr, prev = head2, None

    while curr:
        after_curr = curr.next
        curr.next = prev
        curr, prev = after_curr, curr

    head2 = prev
    slow.next = head2
    return pal


def Detect_Cycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow: return True

    return False

def Length_Of_Cycle(head: ListNode) -> int:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    ## HILARIOUS
    from operator import is_not
    from functools import reduce
    if reduce(is_not, (fast, slow)): return 0

    count = 1
    loop_node = slow
    while slow.next is not loop_node:
        count += 1
        slow = slow.next

    return count


def Intersection_Point(head1: ListNode, head2: ListNode) -> int:

    # attach head1 to head2
    # while you are at it save length of each linked list just in case
    #
    tmp1 = head1
    l1 = 0
    while tmp1.next:
        l1 += 1
        tmp1 = tmp1.next

    tmp1.next = head2 # later this needs to be undone

    slow, fast = head1, head1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slow = head1
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.val

    return -1


def Sort_Linked_List(head: ListNode) -> ListNode:
    freq = [0, 0, 0]
    tmp = head
    while tmp:
        freq[tmp.val] += 1
        tmp = tmp.next

    # no need to make new list
    #

    tmp = head
    for _ in range(freq[0]):
        tmp.val = 0
        tmp = tmp.next
    for _ in range(freq[1]):
        tmp.val = 1
        tmp = tmp.next
    for _ in range(freq[2]):
        tmp.val = 2
        tmp = tmp.next

    return head


def Add_Two_Numbers(head1: ListNode, head2: ListNode) -> ListNode:
    number1 = ""
    number2 = ""

    tmp1, tmp2 = head1, head2
    while tmp1:
        number1 += str(tmp1.val)
        tmp1 = tmp1.next

    while tmp2:
        number2 += str(tmp2.val)
        tmp2 = tmp2.next

    number1 = int(number1)
    number2 = int(number2)
    result = str(number1 + number2)

    ll = ListNode(0)
    tmp = ll
    for char in result:
        tmp.next = ListNode(int(char))
        tmp = tmp.next

    return ll.next


def Rotate(head: ListNode, k: int) -> ListNode:

    length = 0
    tmp = head
    while tmp:
        length += 1
        tmp = tmp.next

    # splice the linked list into two
    k = k % length
    if k == 0: return head

    foot = head
    for _ in range(length - k - 1):
        foot = foot.next

    detached = foot.next
    foot.next = None

    tmp = detached
    while tmp.next:
        tmp = tmp.next

    tmp.next = head
    head = detached
    return head


def reverseKGroup(head: ListNode, k: int) -> ListNode:

    length = 0
    tmp = head
    while tmp:
        length += 1
        tmp = tmp.next

    from math import ceil
    n_groups = int(ceil(length / k))

    groups = [None] * n_groups

    tmp = head
    for i in range(n_groups):
        tmp2 = tmp
        for j in range(k - 1):
            if not tmp2: break
            tmp2 = tmp2.next

        temp = tmp2.next if tmp2 else None
        if tmp2: tmp2.next = None
        groups[i] = tmp
        tmp = temp

    # reverse each group
    for i in range(n_groups):
        curr, prev = groups[i], None
        # check if this group is exactly k elem
        length_ = 0
        tmps = curr
        while tmps:
            length_ += 1
            tmps = tmps.next

        if length_ != k: break


        while curr:
            after_curr = curr.next
            curr.next = prev
            curr, prev = after_curr, curr
        groups[i] = prev

    for i in range(n_groups):
        tmp = groups[i]
        while tmp.next:
            tmp = tmp.next

        if i != n_groups - 1:
            tmp.next = groups[i + 1]

    return groups[0]


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))  #,ListNode(6))))))
print(a)
print(reverseKGroup(a, 3))
