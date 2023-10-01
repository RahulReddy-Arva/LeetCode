"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
The longest depth can only be found by either moving to left or right and getting the count of layers traversed.
Each time we have to only check a couple of things:
1. If the node has left or right?
2.  Each time you go deeper, add +1 to the prev count
3. If you are at the bottom, add 0
4. Also remember that you just need max depth, so the count can be either from left or right - so do a max on either side at each level.
"""


class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
