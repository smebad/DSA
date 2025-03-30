# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Sorting Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
# Time and Space Complexity: 
# O(n log n + m log m) for sorting both strings, where n and m are the lengths of the two strings.
# O(1) or O(n+m) for the space complexity, depending on the sorting algorithm used.

# Test Cases:

# Test Case 1
s = "carrace"
t = "racecar"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: False

# Test Case 2
s = "hello"
t = "world"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: False
