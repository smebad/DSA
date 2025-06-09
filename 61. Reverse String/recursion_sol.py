# Reverse String
# Recursion Solution:

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            if l < r:
                reverse(l + 1, r - 1)
                s[l], s[r] = s[r], s[l]
        
        reverse(0, len(s) - 1)

# Time Complexity: O(n) where n is the length of the string. This is because we need to iterate through the string once to reverse it.
# Space Complexity: O(n) this is because we are using recursion to reverse the string. This recursion will take up to O(n) space in the worst case, where all characters in the string are opening brackets.
# The recursion solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases:
# Test Case 1
s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s) # Expected Output: ["o","l","l","e","h"]

# Test Case 2
s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
print(s) # Expected Output: ["h","a","n","n","a","H"]
