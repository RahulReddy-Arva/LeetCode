"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> [[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]
            for j in range(1, i):
                element = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(element)
            if i > 0:
                row.append(1)
            triangle.append(row)
        return triangle


s = Solution()
numRows = 3
print(f"INPUT  : {numRows} \nOUTPUT : {s.generate(numRows=numRows)}")
