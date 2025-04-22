# Longest Substring Without Repeating Characters
# Brute force solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
    
# Time complexity: O(n * m), where n is the length of the string and m is the length of the longest substring without repeating characters.
# Space complexity: O(m), where m is the length of the longest substring without repeating characters.
# This is because we are using a set to store the characters in the current substring.

# Test Cases:
# Test Case 1:
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # Output: 3

# Test Case 2:
print(s.lengthOfLongestSubstring("bbbbb")) # Output: 1

# Test Case 3:
print(s.lengthOfLongestSubstring("pwwkew")) # Output: 3

