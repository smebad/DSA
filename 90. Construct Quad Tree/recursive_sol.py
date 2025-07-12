# Construct Quad Tree
# Recursive Solution:
from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], True)
            
            n = n // 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)
            
            return Node(0, False, topleft, topright, bottomleft, bottomright)
        
        return dfs(len(grid), 0, 0)
    
# Time Complexity: O(n^2 log n), where n is the length of the grid. The dfs function is called n^2 times, and each call takes O(log n) time to divide the grid into smaller grids. The overall time complexity is O(n^2 log n).
# Space Complexity: O(log n), where n is the length of the grid. The dfs function uses O(log n) space to store the recursion stack.
# This solution uses recursion to divide the grid into smaller grids and construct the Quad-Tree.

# Test Cases
# Test Case 1:
grid = [
    [0, 1],
    [1, 0]
]
# Expected: Non-leaf root, divided into 4 leaves
# Output format (level order): [[0,1],[1,0],[1,1],[1,1],[1,0]]

# Test Case 2:
grid = [
    [1, 1],
    [1, 1]
]
# Expected: A single leaf node representing the whole grid
# Output format: [1,1]

# Test Case 3:
grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# Expected: A single leaf node
# Output format: [1,0]

