# Largest Substring Between Two Equal Characters
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
 

# Constraints:

# 1 <= s.length <= 300
# s contains only lowercase English letters.


# Hash Map Solution:
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}  # char -> first index
        res = -1

        for i, c in enumerate(s):
            if c in char_index:
                res = max(res, i - char_index[c] - 1)
            else:
                char_index[c] = i

        return res
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to check character occurrences and their indices.
# Space Complexity: O(1), since the character set is limited to lowercase English letters (26 characters), leading to constant space usage.
# This hash-map solution efficiently tracks the first occurrence of each character and calculates the maximum length of substrings between equal characters.


# Test Cases
sol = Solution()

# Test Case 1:
s = "aa"
print(sol.maxLengthBetweenEqualCharacters(s))  # Output: 0

# Test Case 2:
s = "abca"
print(sol.maxLengthBetweenEqualCharacters(s))  # Output: 2

# Test Case 3:
s = "cbzxy"
print(sol.maxLengthBetweenEqualCharacters(s))  # Output: -1