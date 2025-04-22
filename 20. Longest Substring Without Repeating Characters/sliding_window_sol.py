# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Sliding Window solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
# Time complexity: O(n), where n is the length of the string.
# Space complexity: O(m), where m is the length of the longest substring without repeating characters.
# This is because we are using a set to store the characters in the current substring.
# The sliding window approach allows us to efficiently find the longest substring without repeating characters by maintaining a window of unique characters.

# Test Cases:
# Test Case 1:
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # Output: 3

# Test Case 2:
print(s.lengthOfLongestSubstring("bbbbb")) # Output: 1

# Test Case 3:
print(s.lengthOfLongestSubstring("pwwkew")) # Output: 3

