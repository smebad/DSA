# has path
# Breadth First Solution:

from collections import deque

def has_path(graph, src, dst):
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False


# Time Complexity:
# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)


# Test Cases:
# Test Case 1:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True

# Test Case 2:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'j')) # False

# Test Case 3:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'i', 'h')) # True


# Test Case 4:
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'w')) # True


# Test Case 5:
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'z')) # False




