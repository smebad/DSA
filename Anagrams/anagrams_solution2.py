# Solution 2

from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

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
