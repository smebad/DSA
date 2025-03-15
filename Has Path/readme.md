# Has Path - Graph Data Structure Problem

## Introduction to Graphs in DSA
A **graph** is a data structure that consists of **nodes (vertices)** connected by **edges**. Graphs can be **directed** (where edges have a direction) or **undirected** (where edges have no direction). They can also be **cyclic** or **acyclic** based on whether they contain cycles. Graphs are widely used in various applications, including networking, pathfinding, and social networks.

## The Has Path Problem
The **Has Path** problem is a fundamental graph traversal problem. Given a **directed acyclic graph** (DAG) represented as an adjacency list and two nodes (`src` and `dst`), the task is to determine whether there exists a directed path from `src` to `dst`.

### Problem Statement:
Write a function, `has_path(graph, src, dst)`, that takes in:
- `graph`: A dictionary representing the adjacency list of a directed acyclic graph.
- `src`: The starting node.
- `dst`: The destination node.

The function should return `True` if there exists a path from `src` to `dst`, otherwise return `False`.

---

## Solution Approaches

### 1. Depth-First Search (DFS) - Recursive Approach
The **Depth-First Search (DFS)** algorithm explores as far as possible along each branch before backtracking. The recursive DFS approach follows these steps:
1. If `src` is equal to `dst`, return `True` (base case).
2. Iterate through all the neighbors of `src`.
3. Recursively check if any neighbor has a path to `dst`.
4. If a path is found, return `True`, otherwise return `False`.

#### DFS Implementation:
```python
# Depth First Search (Recursive)
def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
    
  return False
```

#### Time Complexity:
- **Time Complexity:** `O(e)`, where `e` is the number of edges (each edge is visited once in the worst case).
- **Space Complexity:** `O(n)`, where `n` is the number of nodes (due to recursion depth in the call stack).

---

### 2. Breadth-First Search (BFS) - Iterative Approach
The **Breadth-First Search (BFS)** algorithm explores all neighbors of a node before moving to the next level of nodes. The BFS approach follows these steps:
1. Initialize a queue with `src`.
2. While the queue is not empty, remove the front node and check if it is `dst`.
3. If found, return `True`.
4. Otherwise, add all neighbors to the queue.
5. If the queue is exhausted and no path is found, return `False`.

#### BFS Implementation:
```python
from collections import deque

def has_path(graph, src, dst):
  queue = deque([src])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False
```

#### Time Complexity:
- **Time Complexity:** `O(e)`, where `e` is the number of edges (each edge is visited once).
- **Space Complexity:** `O(n)`, where `n` is the number of nodes (due to queue storage).

---

## Example Test Cases

### Test Case 1
```python
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path(graph, 'f', 'k')) # True
```

### Test Case 2
```python
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path(graph, 'f', 'j')) # False
```

### Test Case 3
```python
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': []
}
print(has_path(graph, 'v', 'w')) # True
print(has_path(graph, 'v', 'z')) # False
```

---

## Summary
- **DFS (Recursive):** Uses recursion to explore all possible paths. It is memory-intensive for deep trees.
- **BFS (Iterative):** Uses a queue for level-order traversal, making it more space-efficient for shallow graphs.
- Both approaches have a **time complexity of O(e)** and **space complexity of O(n)**.
- BFS is generally preferred for finding the shortest path, while DFS is useful for exhaustive path searches.