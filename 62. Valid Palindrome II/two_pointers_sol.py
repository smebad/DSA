# Valid Palindrome II
# Two Pointers Solution:

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True
    
# Time Complexity: O(n) where n is the length of the string. This is because we are using two pointers to iterate through the string once.
# Space Complexity: O(n) this is because we are using only a constant amount of space for the pointers l and r.
# This two pointers solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases:
# Test Case 1:
s = "aba"
print(Solution().validPalindrome(s)) # Expected Output: True

# Test Case 2:
s = "abca"
print(Solution().validPalindrome(s)) # Expected Output: True

# Test Case 3:
s = "abc"
print(Solution().validPalindrome(s)) # Expected Output: False
