# Anagrams Checker

This project is a Python implementation of a function to check if two strings are **anagrams**. Anagrams are strings that contain the same characters but in a different order (e.g., "restful" and "fluster").

## Problem Statement

Write a function, `anagrams`, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams.

---

## Solution

### Approach 1: Dictionary-Based Character Count
```python
def anagrams(s1, s2):
    """
    Function to check if two strings are anagrams.
    Arguments:
    - s1: First string.
    - s2: Second string.
    
    Returns:
    - True if s1 and s2 are anagrams, False otherwise.
    """
    return char_count(s1) == char_count(s2)  # Compare character counts of both strings.

def char_count(s):
    """
    Helper function to count the frequency of characters in a string.
    Argument:
    - s: Input string.
    
    Returns:
    - Dictionary with character counts.
    """
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0  # Initialize the count for new characters.
        count[char] += 1  # Increment the count for each character.
    return count
```

## Approach 2: Using collections.Counter
``` python
from collections import Counter

def anagrams(s1, s2):
    """
    Function to check if two strings are anagrams using Counter.
    Arguments:
    - s1: First string.
    - s2: Second string.
    
    Returns:
    - True if s1 and s2 are anagrams, False otherwise.
    """
    return Counter(s1) == Counter(s2)  # Use Counter to compare character counts.
```

## Test Cases
``` python
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
```

## Complexity:
* Time Complexity: O(n + m)
* Space Complexity: ~O(n + m)

