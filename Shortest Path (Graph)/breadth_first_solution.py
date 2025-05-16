# shortest path
# Breadth First Solution:

from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set([ node_A ])
  queue = deque([ (node_A, 0) ])
  
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


# Time Complexity:
# e = number of edges
# Time: O(e)
# Space: O(e)


# Test Cases
# Test Case 1
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2

# Test Case 2
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'y', 'x')) # -> 1


# Test Case 3
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'a', 'e')) # -> 3


# Test Case 4
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'e', 'c')) # -> 2


# Test Case 5
edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'b', 'g')) # -> -1


# Test Case 6
edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

print(shortest_path(edges, 'w', 'e')) # -> 1


# Test Case 7
edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

print(shortest_path(edges, 'n', 'e')) # -> 2


# Test Case 8
edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

print(shortest_path(edges, 'm', 's')) # -> 6
