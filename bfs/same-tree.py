"""

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = queue.Queue()
        que.put((p, q))

        while not que.empty():
            p, q = que.get()
            if p is None and q is None:
                continue
            if (p is None and q is not None) or (p is not None and q is None):
                return False
            if p.val != q.val:
                return False
            que.put((p.left, q.left))
            que.put((p.right, q.right))
        return True
