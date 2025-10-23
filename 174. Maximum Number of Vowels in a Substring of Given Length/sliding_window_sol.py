# Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length


# Sliding Window Solution:
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}

        l = cnt = res = 0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res, cnt)
        return res
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once. 
# Space Complexity: O(1), since we use a constant amount of space for the variables l, cnt, and res.
# This sliding window approach efficiently counts the number of vowels in each substring of length k and keeps track of the maximum count found.


# Test Cases:
sol = Solution()

# Test Case 1
s1 = "abciiidef"
k1 = 3
print(sol.maxVowels(s1, k1))  # Expected Output: 3

# Test Case 2
s2 = "aeiou"
k2 = 2
print(sol.maxVowels(s2, k2))  # Expected Output: 2

# Test Case 3
s3 = "leetcode"
k3 = 3
print(sol.maxVowels(s3, k3))  # Expected Output: 2