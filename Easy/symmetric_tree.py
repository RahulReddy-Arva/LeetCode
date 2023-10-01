"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if not root:
            return True

        def isSym(node1: TreeNode, node2: TreeNode):
            if not node1 or not node2:
                return node1 == node2
            if node1.val != node2.val:
                return False
            return isSym(node1.left, node2.right) and isSym(node1.right, node2.left)

        return isSym(root.left, root.right)
