# Shortest Path Problem

## Problem Statement
The **Shortest Path** problem requires finding the shortest path (measured in number of edges) between two given nodes in an **undirected graph**. If there is no path between the two nodes, the function should return `-1`.

## Solution Explanation
This problem is best solved using **Breadth-First Search (BFS)** because it explores all neighbors at the present depth level before moving on to nodes at the next depth level. This ensures that the first time we reach the target node, we have found the shortest path.

### Steps to Solve:
1. **Convert the edge list into an adjacency list**: This makes it easier to traverse the graph efficiently.
2. **Initialize a queue for BFS traversal**: Start with the source node (`node_A`) and a distance of `0`.
3. **Use a set to keep track of visited nodes** to avoid cycles and redundant processing.
4. **Perform BFS traversal**:
   - Dequeue a node and check if it is the target node (`node_B`). If yes, return the distance.
   - Otherwise, add all unvisited neighbors to the queue with an incremented distance.
5. **If BFS completes without finding `node_B`**, return `-1` to indicate no path exists.

## Code Implementation
```python
from collections import deque

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A, 0)])
    
    while queue:
        node, distance = queue.popleft()
        
        if node == node_B:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return -1

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
```

## Time Complexity Analysis
- **Building the adjacency list**: `O(e)`, where `e` is the number of edges.
- **Breadth-First Search traversal**: `O(e)`, as each edge is processed once.
- **Overall Complexity**: `O(e)`, which is efficient for sparse graphs.

## Space Complexity
- **Adjacency list storage**: `O(e)`.
- **Queue storage in worst case**: `O(e)`.
- **Visited set storage**: `O(e)`.
- **Overall Complexity**: `O(e)`.

## Example Test Cases
```python
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
print(shortest_path(edges, 'w', 'z'))  # Output: 2
```

## Edge Cases Considered
- **Nodes without any connections**
- **Graphs with cycles**
- **Graphs where `node_A` and `node_B` are disconnected**
- **Small graphs with only one edge**
- **Graphs where `node_A` and `node_B` are the same**

This solution efficiently finds the shortest path in an **undirected, unweighted graph** using BFS.

