###
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200

# strs[i] consists of only lowercase English letters.
###

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        long_string = ""

        # If we sort, the first and last would ideally the least similar - So identifying the pattern between those would give us the solution
        # Initally I misunderstood the requirement to be longest substring which is different from prefix
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first),len(last))):
            if(first[i] != last[i]):
                return long_string
            long_string += first[i]
        return long_string

s = Solution()
p = s.longestCommonPrefix(strs=["flower","flow","flight"])
print(p)