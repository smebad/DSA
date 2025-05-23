# has path
# Depth First Solution:

def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
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




