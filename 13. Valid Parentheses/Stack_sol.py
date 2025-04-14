# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# Stack solution:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
    
# Time Complexity: O(n) where n is the length of the string s. This is because we are iterating through the string once and performing constant time operations for each character.
# Space Complexity: O(n) where n is the length of the string s. This is because we are using a stack to store the opening brackets, which can take up to O(n) space in the worst case.
# The stack will only store the opening brackets, and in the worst case, all characters in the string are opening brackets. In that case, the stack will contain all n characters.
# The stack solution is optimal for large inputs as it takes O(n) time complexity and O(n) space complexity.



# Test Cases:
# Test Case 1
print(Solution().isValid('()')) # True

# Test Case 2
print(Solution().isValid('()[]{}')) # True

# Test Case 3
print(Solution().isValid('(]')) # False

# Test Case 4
print(Solution().isValid('([])')) # True