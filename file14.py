# binary tree problems
#
#
from __future__ import annotations

class Binary_Node:
    def __init__(self, data, left: Binary_Node | None = None, right: Binary_Node | None = None):
        self.data, self.left, self.right = data, left, right

r'''

              1
            /---\
            2    3
            /\   /
            4 5  6
'''

node = Binary_Node(1)
node2 = Binary_Node(2)
node3 = Binary_Node(3)
node4 = Binary_Node(4)
node5 = Binary_Node(5)
node6 = Binary_Node(6)
node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

def Inorder(root: Binary_Node):
    if not root: return

    Inorder(root.left)
    print(root.data)
    Inorder(root.right)

def Preorder(root: Binary_Node):
    if not root: return

    print(root.data)
    Preorder(root.left)
    Preorder(root.right)

def Postorder(root: Binary_Node):
    if not root: return

    Postorder(root.left)
    Postorder(root.right)
    print(root.data)

def Levelorder(root: Binary_Node):
    from collections import deque
    d = deque([root])

    while d:
        node = d.popleft()
        print(node.data)
        if node.left: d.append(node.left)
        if node.right: d.append(node.right)


def Depth_Tree(root: Binary_Node):

    def _depth(node: Binary_Node | None, curr_depth: int) -> int:
        if not node: return curr_depth
        left_depth, right_depth = 1 + _depth(node.left, curr_depth), 1 + _depth(node.right, curr_depth)
        return max(left_depth, right_depth)

    return _depth(root, 0)

def Maximum_Width(root: Binary_Node) -> int:
    from collections import deque
    d = deque((root,))
    max_width = 1

    while d:
        max_width = max(max_width, len(d))
        for _ in range(len(d)):
            node = d.popleft()
            if node.left: d.append(node.left)
            if node.right: d.append(node.right)

    return max_width


# These are naive implementations, think recursively now
# def Balanced(root: Binary_Node):

#     def _balanced(node: Binary_Node | None, curr_height: int) -> int | bool:
#         if not node: return curr_height
#         left_height = 1 + _balanced(node.left, curr_height)
#         right_height = 1 + _balanced(node.right, curr_height)
#         if abs(left_height - right_height) >= 1: return False
#         return True

#     return _balanced(root, 0)
#

def Balanced(root: Binary_Node | None) -> int:
    if not root: return 0
    left_height = Balanced(root.left)
    right_height = Balanced(root.right)
    if abs(left_height - right_height) > 1: return -1
    return max(left_height, right_height) + 1

def Identical(root1: Binary_Node | None, root2: Binary_Node | None) -> bool:
    if not root1 and not root2: return True
    elif not root1 or not root2: return False
    else: return (root1.data == root2.data) and Identical(root1.left, root2.left) and Identical(root1.right, root2.right)

def Sum(root: Binary_Node | None) -> int:
    if not root: return 0
    if not root.left or not root.right: return root.data
    ls, rs = Sum(root.left), Sum(root.right)
    if ls == -1 or rs == -1: return -1
    if ls + rs != root.data: return -1
    return ls + rs + root.data

def Left_View(root: Binary_Node):
    ## level order traversal
    from collections import deque
    d = deque((root,))
    while d:
        for i in range(len(d)):
            node = d.popleft()
            if i == 0: print(node.data)
            if node.left: d.append(node.left)
            if node.right: d.append(node.right)

def Root_To_Leaf_Path_Sum(root: Binary_Node, k: int) -> bool:

    def _inorder(node: Binary_Node | None, target: int) -> bool:
        if not node: return False
        target -= node.data

        if not node.left and not node.right: return target == 0
        return _inorder(node.left, target) or _inorder(node.right, target)

    return _inorder(root, k)

# Preorder(node)

def Iter_Preorder(root: Binary_Node):
    stack = [ root ]

    while stack:
        node = stack.pop()
        print(node.data)

        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

def Iter_Inorder(root: Binary_Node):

    tmp = root
    stack = []

    while tmp or stack:
        while tmp:
            stack.append(tmp)
            tmp = tmp.left

        tmp = stack.pop()
        print(tmp.data)

        tmp = tmp.right


def Sum_Of_Nodes_On_Longest_Path(root: Binary_Node) -> int:

    def _sum(node: Binary_Node | None, height: int, csum: int) -> tuple[int, int]:
        if not node: return height, csum

        left = _sum(node.left, height + 1, csum + node.data)
        right = _sum(node.right, height + 1, csum + node.data)

        if left[0] > right[0]: return left
        elif right[0] > left[0]: return right
        else: return left if left[1] > right[1] else right

    return _sum(root, 0, 0)[1]

from memory_profiler import profile

@profile
def Max_Diameter(root: Binary_Node) -> int:

    def _height(node: Binary_Node | None) -> int:
        if not node: return 0
        return 1 + max( _height(node.left), _height(node.right) )

    def _diameter(node: Binary_Node | None) -> int:
        if not node: return 0
        lh, rh = _height(node.left), _height(node.right)
        ld, rd = _diameter(node.left), _diameter(node.right)
        return max(ld, rd, lh + rh)

    return _diameter(root)

print(Max_Diameter(node))

# nodex = Binary_Node(4)
# nodex1 = Binary_Node(2)
# nodex2 = Binary_Node(5)
# nodex3 = Binary_Node(7)
# nodex4 = Binary_Node(1)
# nodex5 = Binary_Node(2)
# nodex6 = Binary_Node(3)
# nodex7 = Binary_Node(6)
# nodex.left, nodex.right = nodex1, nodex2
# nodex1.left, nodex1.right = nodex3, nodex4
# nodex4.left = nodex7
# nodex2.left, nodex2.right = nodex5, nodex6
# assert(Sum_Of_Nodes_On_Longest_Path(nodex) == 13)
