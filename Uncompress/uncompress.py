# uncompress
# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.


# solution (using two pointers)
def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:      
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
      
  return ''.join(result)

# Test Cases
# Test Case 0
print(uncompress("2c3a1t")) # -> 'ccaaat'

# Test Case 1
print(uncompress("4s2b")) # -> 'ssssbb'

# Test Case 2
print(uncompress("2p1o5p")) # -> 'ppoppppp'

# Test Case 3
print(uncompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'

# Test Case 4
print(uncompress("127y")) # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

# Time Complexity:
# n = number of groups
# m = max number found in any group
# Time: O(n * m)
# Space: O(n * m)