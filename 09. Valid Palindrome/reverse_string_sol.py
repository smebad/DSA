# Valid Palindrome

# reverse string solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
# Time complexity: O(n), where n is the length of the string s.
# Space complexity: O(n), where n is the length of the string s.

# Test Cases:
# Test Case 1
print(Solution().isPalindrome('A man, a plan, a canal: Panama')) # True

# Test Case 2
print(Solution().isPalindrome('race a car')) # False

# Test Case 3
print(Solution().isPalindrome(' ')) # True
