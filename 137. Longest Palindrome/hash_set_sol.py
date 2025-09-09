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


# Hash-Set Solution:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)

        return res + 1 if seen else res

# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to check character occurrences.
# Space Complexity: O(m), where m is the number of unique characters in the string s. In the worst case, all characters are unique, leading to O(n) space usage.
# This hash-set solution efficiently tracks character occurrences and determines the length of the longest palindrome that can be formed.



# Test Cases
sol = Solution()

# Test Case 1:
s = "abccccdd"
print(sol.longestPalindrome(s))  # Output: 7

# Test Case 2:
s = "a"
print(sol.longestPalindrome(s))  # Output: 1