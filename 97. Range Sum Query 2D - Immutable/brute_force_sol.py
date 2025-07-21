# Range Sum Query 2D - Immutable
# Brute Force Solution:
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                res += self.matrix[r][c]
        return res
    
# Time Complexity: O(m * n) for each query, where m is the number of rows and n is the number of columns in the submatrix defined by the query. This is because we need to iterate over the entire submatrix to compute the sum.
# Space Complexity: O(1) since we are not using any additional data structures.
# This brute force solution is efficient for small matrices or when the number of queries is low, but it can be slow for larger matrices or a high number of queries.


# Test Case:
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12
