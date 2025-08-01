# Search a 2D Matrix
# Brute force solution:

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
    
# Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
# Space complexity: O(1) as we are not using any extra space.
# This brute force solution is not optimal and can be improved using binary search.
# The brute force solution has a time complexity of O(m*n) which is not efficient for large matrices.


# Test Cases:
# Test case 1: 
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
print(sol.searchMatrix(matrix, target))  # Output: True

# Test case 2:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
sol = Solution()
print(sol.searchMatrix(matrix, target))  # Output: False

# Test case 3:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 1
sol = Solution()
print(sol.searchMatrix(matrix, target))  # Output: True
