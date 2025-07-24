# Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

# Dynamic Programming Solution:
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
    
# Time Complexity: O(numRows^2) where numRows is the number of rows in Pascal's triangle. This is because we are constructing each row based on the previous row, leading to a quadratic growth in the number of operations.
# Space Complexity: O(numRows^2) for storing the entire triangle in a list of lists. Each row i contains i + 1 elements, leading to a total of numRows * (numRows + 1) / 2 elements in the triangle.
# This dynamic programming solution is efficient and straightforward, leveraging the properties of Pascal's triangle to build each row based on the previous one.

# Test cases
# Test Case 1:
print(Solution().generate(5)) # -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Test Case 2:
print(Solution().generate(1)) # -> [[1]]