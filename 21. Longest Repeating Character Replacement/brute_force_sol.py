# Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


# Brute Force Solution:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
    
# Time Complexity: O(n^2) where n is the length of s which is the number of characters in the string.
# Space Complexity: O(m) where m is the number of unique characters in the string.
# In the worst case, m can be 26 (for uppercase English letters).
# So, the space complexity can be considered O(1) in this case.
# Brute force solution is not optimal and can be improved using sliding window technique.


# Test Cases:
# Test Case 1:
s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k)) # Expected Output: 4

# Test Case 2:
s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k)) # Expected Output: 4
