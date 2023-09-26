###
# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
###


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return "".join(set([i for i in s]))

    def remove_duplicate_chars(self, input_str: str) -> str:
        stack = []
        seen = set()
        char_counts = {}

        for i in input_str:
            char_counts[i] = char_counts.get(i, 0) + 1

        for i in input_str:
            char_counts[i] -= 1
            if i in seen:
                continue
            while stack and i < stack[-1] and char_counts[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(i)
            seen.add(i)
        return "".join(stack)


s = Solution()
i = "cbacdcbc"
p = s.remove_duplicate_chars(i)
print(f"INPUT  : {i}\nOUTPUT : {p}")
