# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


# Stack Solution:
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1

# Time Complexity: O(n) where n is the length of the string. This is because we need to iterate through the string once to reverse it.
# Space Complexity: O(n) this is because we are using a stack to store the characters. This stack will take up to O(n) space in the worst case, where all characters in the string are opening brackets.
# The stack solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases:
# Test Case 1
s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s) # Expected Output: ["o","l","l","e","h"]

# Test Case 2
s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
print(s) # Expected Output: ["h","a","n","n","a","H"]