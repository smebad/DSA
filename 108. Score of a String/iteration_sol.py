# Score of a String
# Iteration solution:
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))
        return res
    
# Time Complexity: O(n), where n is the length of the string s. This is because we are iterating through the string once to calculate the score.
# Space Complexity: O(1), as we are using only a constant amount of space for the result variable.
# This iterative approach efficiently calculates the score of the string by summing the absolute differences between the ASCII values of adjacent characters. It is optimal for the problem at hand.

# Test Cases
# Test Case 1:
s1 = "hello"
sol = Solution()
print(sol.scoreOfString(s1))  # Expected output: 13

# Test Case 2:
s2 = "zaz"
print(sol.scoreOfString(s2))  # Expected output: 50
