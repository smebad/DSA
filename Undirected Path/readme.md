# Undirected Path

## Problem Statement
Write a function, `undirected_path`, that takes in a list of edges representing an undirected graph and two nodes (`node_A`, `node_B`). The function should return a boolean indicating whether or not there exists a path between `node_A` and `node_B`.

## Understanding Undirected Paths in Graphs
Graphs are a collection of nodes (vertices) connected by edges. In an **undirected graph**, edges do not have a direction, meaning that if there is an edge between `A` and `B`, you can travel from `A` to `B` and vice versa.

The problem of finding an undirected path requires checking if there is a way to traverse the graph from `node_A` to `node_B`, considering the given edges.

## Solution Explanation
This problem can be solved efficiently using **Depth-First Search (DFS)**. The approach consists of the following steps:

1. **Convert the list of edges into an adjacency list** (graph representation).
2. **Perform DFS traversal** starting from `node_A`.
3. **Use a set to keep track of visited nodes** to avoid cycles and redundant calculations.
4. **Recursively explore neighboring nodes** until `node_B` is found or all paths are exhausted.

### Implementation
The solution consists of three main functions:
1. **`build_graph(edges)`**
   - Converts the list of edges into an adjacency list (dictionary) where each key represents a node and maps to a list of connected nodes.

2. **`has_path(graph, src, dst, visited)`**
   - Performs recursive DFS to determine if there is a path between `src` and `dst`.
   - If `src` is `dst`, return `True`.
   - If `src` has already been visited, return `False`.
   - Mark `src` as visited.
   - Recursively check all neighbors for a path.

3. **`undirected_path(edges, node_A, node_B)`**
   - Calls `build_graph()` to construct the graph.
   - Calls `has_path()` to check for a path between `node_A` and `node_B`.

### Code Implementation
```python
# Depth First Solution:
def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

def build_graph(edges):
    graph = {}
    
    for edge in edges:
        a, b = edge
        
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
        
    return graph
    
def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True
    
    return False
```

## Time Complexity Analysis
- **Building the Graph (`build_graph`)**: Since each edge is processed once, this takes **O(e)** time, where `e` is the number of edges.
- **DFS Traversal (`has_path`)**: In the worst case, we visit all nodes and edges, leading to a time complexity of **O(e)**.
- **Overall Time Complexity**: **O(e)**, since both functions combined run in linear time.
- **Space Complexity**: **O(e)** for storing the adjacency list and visited set.

## Example Test Cases
```python
# Test Case 1
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(undirected_path(edges, 'j', 'm')) # -> True

# Test Case 2
print(undirected_path(edges, 'k', 'o')) # -> False

# Test Case 3
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]
print(undirected_path(edges, 'r', 't')) # -> True
```

## Conclusion
This solution effectively finds a path in an undirected graph using **Depth-First Search (DFS)**. It efficiently constructs the graph and searches for a connection between two nodes in **O(e)** time. The approach ensures optimal performance while handling various edge cases in graph traversal.

