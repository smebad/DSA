# Solution
def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}

  for char in s:
    if char not in count:
      count[char] = 0

    count[char] += 1

  return count

# print( char_count('catss)) # {'c': 1, 'a': 2, 't': 2, 's': 1}

# Test Cases
# Test Case 0
print(anagrams('restful', 'fluster'))  # -> True
# Test Case 1
print(anagrams('cats', 'tocs')) # -> False
# Test Case 2
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
# Test Case 3
print(anagrams('paper', 'reapa')) # -> False
# Test Case 4
print(anagrams('elbow', 'below')) # -> True
# Test Case 5
print(anagrams('tax', 'taxi')) # -> False
# Test Case 6
print(anagrams('taxi', 'tax')) # -> False
# Test Case 7
print(anagrams('night', 'thing')) # -> True
# Test Case 8
print(anagrams('abbc', 'aabc')) # -> False
# Test Case 9
print(anagrams('po', 'popp')) # -> false
# Test Case 10
print(anagrams('pp', 'oo')) # -> false


# Complexity:
# n = strings1 length
# m = strings2 length
# Time: O(n + m)
# Space: ~O(n + m)
# Linear Solution!
