# Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


# Recursive Solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def rec(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            
            if s[i] == t[j]:
                return rec(i + 1, j + 1)
            return rec(i, j + 1)
        return rec(0, 0)
    
# Time Complexity: O(n * m), where n is the length of s and m is the length of t. This is because we are exploring all combinations of characters in s and t.
# Space Complexity: O(n + m), due to the recursion stack which can go as deep as the lengths of s and t.
# This recursive approach checks if s is a subsequence of t by recursively comparing characters and moving through both strings. If we reach the end of s, it confirms that s is a subsequence of t. However, this solution is less efficient than the two-pointer technique due to its higher time complexity and space usage.


# Test Cases
# Test Case 1:
s1 = "abc"
t1 = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s1, t1))  # Expected output: True

# Test Case 2:
s2 = "axc"
t2 = "ahbgdc"
print(sol.isSubsequence(s2, t2))  # Expected output: False