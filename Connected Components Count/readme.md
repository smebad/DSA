# Connected Components Count

## Problem Statement
The **Connected Components Count** problem is a fundamental problem in graph theory. Given an **undirected graph** represented as an **adjacency list**, we need to determine the number of **connected components** in the graph.

### What is a Connected Component?
A **connected component** in an undirected graph is a **subset of nodes** such that there is a path between any two nodes within this subset. Additionally, no node in this subset has a connection to nodes outside the subset. In simple terms, it is a group of nodes that are connected directly or indirectly but isolated from other groups.

## Solution Explanation
### Approach Used: **Depth-First Search (DFS)**
To determine the number of connected components, we perform a **Depth-First Search (DFS)** on the graph.

### Steps:
1. **Initialize a `visited` set** to keep track of visited nodes.
2. **Iterate over each node** in the graph:
   - If the node has **not been visited**, we call the `explore` function to traverse its connected component.
   - If `explore` returns `True`, it means we discovered a new component, so we **increment the count**.
3. **DFS Traversal (`explore` function):**
   - If the current node has already been visited, return `False`.
   - Otherwise, add the node to the `visited` set.
   - Recursively explore all its neighbors.
   - Return `True` after fully exploring the component.

### Python Implementation:
```python
# Depth-First Search Solution:
def connected_components_count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1
      
  return count

def explore(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
  
  return True
```

## Time and Space Complexity Analysis
### **Time Complexity:**
- **O(e + n)** where:
  - `n` is the number of nodes (vertices)
  - `e` is the number of edges
- Each node is visited once, and all edges are processed, leading to **O(e + n) complexity**.

### **Space Complexity:**
- **O(n)** due to:
  - The `visited` set storing up to `n` nodes.
  - The recursive function stack consuming at most `O(n)` space in the worst case (if the graph is a long chain).

## Example Test Cases
```python
# Example 1:
print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # Output: 2

# Example 2:
print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # Output: 1

# Example 3:
print(connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # Output: 3

# Example 4:
print(connected_components_count({})) # Output: 0

# Example 5:
print(connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
})) # Output: 5
```

## Summary
- We used **Depth-First Search (DFS)** to explore connected components.
- **Time Complexity:** `O(e + n)`, where `e` is the number of edges and `n` is the number of nodes.
- **Space Complexity:** `O(n)` due to the recursion stack and visited nodes.
- This algorithm efficiently determines the number of connected components in an **undirected graph**.