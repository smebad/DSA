# Most frequent char
# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

# Approach 2

from collections import Counter

def most_frequent_char(s):
  count = Counter(s)

  max_value = None
  for char in s:
    if max_value is None or count[char] > count[max_value]:
      max_value = char
  return max_value

# Test Cases
# Test Case 1
print(most_frequent_char('bookeeper')) # 'e'

# Test Case 2
print(most_frequent_char('david')) # 'd'

# Test Case 3
print(most_frequent_char('abby')) # 'b'

# Test Case 4
print(most_frequent_char('mississippi')) # 'i'

# Test Case 5
print(most_frequent_char('eleventennine')) # 'e'

# Test Case 6
print(most_frequent_char('riverbed')) # 'r'

# Complexity
# n = length of string
# Time: O(n)
# Space: O(n)
# Linear Time Linear Space!