# Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Binary Search solution:
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
    
# Time complexity: O(log(m) + log(n)) where m is the number of rows and n is the number of columns in the matrix.
# Space complexity: O(1) as we are not using any extra space.
# This binary search solution is optimal and has a time complexity of O(log(m) + log(n)) which is efficient for large matrices.
# Why this solution is better and optimal than brute force solution: Because it uses binary search to find the target in a sorted matrix, reducing the time complexity from O(m*n) to O(log(m) + log(n)).
# The binary search solution is more efficient than the brute force solution as it reduces the number of comparisons needed to find the target.


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