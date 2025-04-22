# Longest Substring Without Repeating Characters
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

