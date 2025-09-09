# Longest Palindrome
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
