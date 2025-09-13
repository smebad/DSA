# First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


# Hash-Map Solution:
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string twice, once to count the occurrences of each character and once to find the first unique character.
# Space Complexity: O(1), since the character set is limited to lowercase English letters, the size of the hashmap will not exceed 26 entries.
# This hash-map solution efficiently tracks character frequencies and finds the first unique character in the string.


# Test Cases
sol = Solution()

# Test Case 1:
s = "leetcode"
print(sol.firstUniqChar(s))  # Expected output: 0

# Test Case 2:
s = "loveleetcode"
print(sol.firstUniqChar(s))  # Expected output: 2

# Test Case 3:
s = "aabb"
print(sol.firstUniqChar(s))  # Expected output: -1