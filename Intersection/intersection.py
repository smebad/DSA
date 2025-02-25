# Solution brute force (timeout)
def intersection(a, b):
  result = []
  for item in b:
    if item in a:
      result.append(item)
  return result

# Test Cases
# Test Case 1
print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]

# Test Case 2
print(intersection([2,4,6], [4,2])) # -> [2,4]

# Test Case 3
print(intersection([4,2,1], [1,2,4,6])) # -> [1,2,4]

# Test Case 4
print(intersection([0,1,2], [10,11])) # -> []

# Test Case 5
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
print(intersection(a, b)) # -> [0,1,2,3,..., 49999]

# Time Complexity:
# n = length of array a, m = length of array b
# Time: O(n*m)
# Space: O(min(n,m))