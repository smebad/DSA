# Compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'''
'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
'''
# You can assume that the input only contains alphabetic characters.

# Solution

def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) 
        result.append(s[i])
      i = j
    
  return ''.join(result)





# Test Cases
# Test Case 1
print(compress('ccaaatsss')) # -> '2c3at3s'

# Test Case 2
print(compress('ssssbbz')) # -> '4s2bz'

# Test Case 3
print(compress('ppoppppp')) # -> '2po5p'

# Test Case 4
print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'

# Test Case 5
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')); # -> '127y'


# Time Complexity:
# n = length of string
# Time: O(n)
# Space: O(n)