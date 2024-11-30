# pair sum problem
# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

# Library using solution

def pair_sum(numbers, target_sum):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous_numbers:
      return (index, previous_numbers[complement])
    
    previous_numbers[num] = index




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
# n = length of numbers list
# Time: O(n)
# Space: O(n)