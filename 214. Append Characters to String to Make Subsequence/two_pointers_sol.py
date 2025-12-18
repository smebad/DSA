# Append Characters to String to Make Subsequence
# You are given two strings s and t consisting of only lowercase English letters.

# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

# Example 1:

# Input: s = "coaching", t = "coding"
# Output: 4
# Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
# Example 2:

# Input: s = "abcde", t = "a"
# Output: 0
# Explanation: t is already a subsequence of s ("abcde").
# Example 3:

# Input: s = "z", t = "abcde"
# Output: 5
# Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
# Now, t is a subsequence of s ("zabcde").
# It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
 

# Constraints:

# 1 <= s.length, t.length <= 105
# s and t consist only of lowercase English letters.
 

# Two pointers solution:
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j
    
# Time complexity: O(n + m), where n and m are the lengths of strings s and t respectively.
# Space complexity: O(1), as we are using only a constant amount of extra space.
# This two pointers approach is efficient and works well within the given constraints.


# Test Cases:
# Test Case 1:
s1 = "coaching"
t1 = "coding"
print(Solution().appendCharacters(s1, t1))  # Output: 4

# Test Case 2:
s2 = "abcde"
t2 = "a"
print(Solution().appendCharacters(s2, t2))  # Output: 0

# Test Case 3:
s3 = "z"
t3 = "abcde"
print(Solution().appendCharacters(s3, t3))  # Output: 5