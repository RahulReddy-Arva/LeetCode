"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of roots along the shortest path from the root root down to the nearest leaf root.
Note: A leaf is a root with no children.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 2

Example 2:
    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5

Constraints:
    The number of roots in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
