# binary tree
#
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    left: Node | None = None
    right: Node | None = None

node = Node(100)
node1 = Node(200)
node2 = Node(300)
node3 = Node(400)
node4 = Node(500)

node.left = node1
node.right = node2
node1.left = node3
node1.right = node4

def inorder(n: Node | None):
    if not n: return
    inorder(n.left)
    print(n.data)
    inorder(n.right)

def preorder(n: Node | None):
    if not n: return
    print(n.data)
    preorder(n.left)
    preorder(n.right)

def postorder(n: Node | None):
    if not n: return
    postorder(n.left)
    postorder(n.right)
    print(n.data)

def levelorder(n: Node | None, l: int, res: []):
    if not n: return
    if len(res) <= l: res.append([])
    res[l].append(n.data)

    levelorder(n.left, l + 1, res)
    levelorder(n.right, l + 1, res)

def Size_Of_Binary_Tree(node: Node | None) -> int:
    if not node: return 0
    return 1 + Size_Of_Binary_Tree(node.left) + Size_Of_Binary_Tree(node.right)

def Max_Depth(node: Node | None, curr_depth) -> int:
    if not node: return -1
    return max(curr_depth, 1 + Max_Depth(node.left, curr_depth), 1 + Max_Depth(node.right, curr_depth))

def Max_Width(node: Node) -> int:
    res = []
    levelorder(node, 0, res)
    res.sort(key=len)
    return len(res[-1])

def Check_Balanced(node: Node) -> bool:
    # true for balanced
    #
    def height(_node: Node | None) -> int:
        if not _node: return 0
        l_height = height(_node.left)
        r_height = height(_node.right)

        if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1: return -1
        return 1 + max(l_height, r_height)

    if height(node) == -1: return False
    return True
