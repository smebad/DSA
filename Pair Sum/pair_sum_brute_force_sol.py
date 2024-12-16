# pair sum problem
# Write a function, pair_sum, that takes in a list and 
# Brute Force Solution

def pair_sum(numbers, target_sum):
  for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i, j)

# Test cases
# Test Case 0
print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)

# Test Case 1
print(pair_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)

# Test Case 2
print(pair_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)

# Test Case 3
print(pair_sum([1, 6, 7, 2], 13)) # -> (1, 2)

# Test Case 4
print(pair_sum([9, 9], 18)) # -> (0, 1)

# Test Case 5
print(pair_sum([6, 4, 2, 8 ], 12)) # -> (1, 3)

# Test Case 6
numbers = [ i for i in range(1, 6001) ]
print(pair_sum(numbers, 11999)) # -> (5998, 5999)

# Time Complexity:
# n = 
# Time:
# Space: