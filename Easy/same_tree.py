"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        def ist(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val == node2.val:
                return ist(node1.left, node2.left) and ist(node1.right, node2.right)
            return False

        return ist(p,q)