"""
Given a binary tree, determine if it is height-balanced (A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.)

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

Example 3:
    Input: root = []
    Output: true

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, node: [TreeNode]) -> int:
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if abs(left-right) > 1 or left == -1 or right == -1:
            return -1
        return 1 + max(left, right)
