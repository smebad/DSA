# Solution - recursive
def sum_numbers_recursive(numbers):
  if len(numbers) == 0:
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])


# Test Cases
# Test Case 1
print(sum_numbers_recursive([5, 2, 9, 10])) # -> 26

# Test Case 2
print(sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1])) # -> 1

# Test Case 3
print(sum_numbers_recursive([])) # -> 0

# Test Case 4
print(sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1])) # -> 1001

# Test Case 5
print(sum_numbers_recursive([700, 70, 7])) # -> 777

# Test Case 6
print(sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])) # -> -55

# Test Case 7
print(sum_numbers_recursive([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # -> 0

# Test Case 8
print(sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0])) # -> 137174205

# Time Complexity:
# Time: O(n^2)
# Space: O(n^2)

