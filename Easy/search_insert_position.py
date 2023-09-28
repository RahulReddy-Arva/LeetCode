###
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
###

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # Null checks
        if nums[-1] < target:
          return len(nums)
        if nums[0] > target or len(nums) == 0:
          return 0
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        # Binary search has been used as the req is to get the results in O(logN)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right == mid:
            return mid+1
        else:
          return mid

s = Solution()
p = s.searchInsert(nums = [1,3,5,6], target = 2)
print(p)