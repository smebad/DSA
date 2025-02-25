# Pair product

# Solution
def pair_product(numbers, target_product):
  previous_nums = {}
  
  for index, num in enumerate(numbers):
    complement = target_product / num
    
    if complement in previous_nums:
      return (index, previous_nums[complement])
    
    previous_nums[num] = index



# Test cases
# Test Case 0
print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)

# Test Case 1
print(pair_product([3, 2, 5, 4, 1], 10)) # -> (1, 2)

# Test Case 2
print(pair_product([3, 2, 5, 4, 1], 10)) # -> (1, 2)

# Test Case 3
print(pair_product([4, 7, 9, 2, 5, 1], 35)) # -> (1, 4)

# Test Case 4
print(pair_product([3, 2, 5, 4, 1], 10)) # -> (1, 2)

# Test Case 5
print(pair_product([4, 6, 8, 2], 16)) # -> (2, 3)

# Test Case 6
numbers = [ i for i in range(1, 6001) ]
print(pair_product(numbers, 35994000)) # -> (5998, 5999) 

# Time Complexity:
# n = length of numbers list
# Time: O(n)
# Space: O(n)
# Linear Time Linear Space