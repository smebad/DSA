# Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


# Hash Map Solution:
from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2

        return res + (res < len(s))
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to count character frequencies.
# Space Comeplexity: O(m), where m is the number of unique characters in the string s. In the worst case, all characters are unique, leading to O(n) space usage.
# This hash-map solution efficiently counts character frequencies and determines the length of the longest palindrome that can be formed.


# Test Cases
sol = Solution()

# Test Case 1:
s = "abccccdd"
print(sol.longestPalindrome(s))  # Output: 7

# Test Case 2:
s = "a"
print(sol.longestPalindrome(s))  # Output: 1