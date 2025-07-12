# Construct Quad Tree - LeetCode

## Problem Statement

Given an `n x n` binary matrix `grid` consisting only of `0`s and `1`s, the goal is to represent this grid using a **Quad Tree** and return the root node of the tree.

A **Quad Tree** is a tree data structure in which each internal node has exactly four children representing four quadrants: topLeft, topRight, bottomLeft, and bottomRight. Each node also contains:

* `val`: True if the grid represented is full of 1s, False if it's full of 0s.
* `isLeaf`: True if the node is a leaf node, False otherwise.

## What Does "Construct Quad Tree" Mean?

Constructing a quad tree from a grid means recursively dividing the grid into quadrants until all elements in a quadrant are the same. If a subgrid has the same value throughout, it is represented as a leaf node.

## Code Explanation

```python
from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
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
```

### Code

* `dfs(n, r, c)` is a recursive function that works on a subgrid starting at `(r, c)` with size `n`.
* `allSame` checks if the current subgrid has all the same values.
* If yes, return a leaf node with that value.
* If not, divide the grid into 4 parts and recursively build each.

## Solution and Logic in Simple Words

* If all values in a grid are the same, there's no need to divide it further.
* Otherwise, divide the grid into four equal subgrids.
* Repeat this process recursively for each subgrid.
* Assemble the results into a node with 4 children.

### Difference Between Nodes

* **Leaf node**: has `isLeaf=True` and no children.
* **Internal node**: has `isLeaf=False` and 4 children.

## Time and Space Complexity

* **Time Complexity**: `O(n^2 log n)`

  * At most, `O(n^2)` nodes are processed.
  * Each recursive division splits the grid, leading to `log n` levels.

* **Space Complexity**: `O(log n)`

  * Due to the recursion stack depth which can go up to `log n` levels.

### Most Optimal Solution

This recursive divide-and-conquer approach is the most optimal for this problem because:

* It avoids unnecessary divisions when a region is uniform.
* It directly follows the definition and constraints of a quad tree.

## Simple Test Cases

```python
# Test Case 1
# Grid: all values are the same -> should return a single leaf node
[[1, 1],
 [1, 1]]
# Output: Node(val=1, isLeaf=True)

# Test Case 2
# Grid: mixed values -> should return an internal node with 4 children
[[0, 1],
 [1, 0]]
# Output: Node(isLeaf=False), with 4 children that are all leaves

# Test Case 3
# Grid: all zero
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
# Output: Node(val=0, isLeaf=True)
```
