# Longest Palindrome
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
