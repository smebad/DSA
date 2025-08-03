# Score of a String
# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.

 

# Example 1:

# Input: s = "hello"

# Output: 13

# Explanation:

# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:

# Input: s = "zaz"

# Output: 50

# Explanation:

# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

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