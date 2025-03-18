# Largest Component

## Problem Statement
The **Largest Component** problem involves finding the size of the largest connected component in an undirected graph represented as an adjacency list. A **connected component** is a subset of nodes such that there is a path between any two nodes in that subset, and no additional nodes outside of it are connected to it.

### Example
Given the graph:
```python
{
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
```
The largest connected component has **4** nodes.

## Solution Explanation
The solution uses **Depth-First Search (DFS)** to explore connected components and determine their sizes. The algorithm follows these steps:
1. **Iterate through all nodes**: For each unvisited node, initiate a DFS traversal to calculate the size of the connected component it belongs to.
2. **Use DFS for exploration**: The `explore_size` function recursively visits all reachable nodes and calculates the component size.
3. **Track the largest component**: Compare the size of each component with the largest size found so far and update accordingly.

### Python Implementation
```python
def largest_component(graph):
  visited = set()
  largest = 0
  
  for node in graph:
    size = explore_size(graph, node, visited)
    if size > largest:
      largest = size
  
  return largest

def explore_size(graph, node, visited):
  if node in visited:
    return 0
  
  visited.add(node)
  
  size = 1
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)
    
  return size
```

## Time and Space Complexity
- **Time Complexity:** **O(e)** where `e` is the number of edges (since every edge is visited once).
- **Space Complexity:** **O(n)** where `n` is the number of nodes (to store visited nodes).

## Example Test Cases
```python
print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4

print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6

print(largest_component({})) # -> 0
```

## Summary
- This problem helps in understanding **graph traversal techniques**, particularly **DFS**.
- The approach efficiently finds the largest connected component by exploring all reachable nodes recursively.
- **Time Complexity: O(e)** and **Space Complexity: O(n)** ensure efficiency for large graphs.

