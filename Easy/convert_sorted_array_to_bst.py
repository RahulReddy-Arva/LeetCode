"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Simple explanation from Google (This can be applied to lists also):
1) Get the Middle of the linked list and make it root.
2) Recursively do same for the left half and right half.
       a) Get the middle of the left half and make it left child of the root
          created in step 1.
       b) Get the middle of right half and make it the right child of the
          root created in step 1.
"""


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> [TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        # Construct the tree with mid as current node each time
        root: TreeNode = TreeNode(nums[mid])
        # Assign all elements in list till mid to left
        root.left = self.sortedArrayToBST(nums[:mid])
        # Assign all elements in list from mid to end to right
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
