# Valid Palindrome

# Two Pointers solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    # or we could write return isalnum(c) instead of the above function

# Time complexity: O(n), where n is the length of the string s.
# Space complexity: O(n), where n is the length of the string s.

# Test Cases:
# Test Case 1
print(Solution().isPalindrome('A man, a plan, a canal: Panama')) # True

# Test Case 2
print(Solution().isPalindrome('race a car')) # False

# Test Case 3
print(Solution().isPalindrome(' ')) # True
