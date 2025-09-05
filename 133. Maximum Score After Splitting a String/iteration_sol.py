# Maximum Score After Splitting a String
# Iteration Solution:
class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count('1')
        res = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)

        return res
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to count the number of '1's and then again to calculate the maximum score.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This solution efficiently calculates the maximum score by maintaining counts of '0's in the left substring and '1's in the right substring as we iterate through the string.

# Test Cases
sol = Solution()

# Test Case 1:
s = "011101"
print(sol.maxScore(s))  # Expected output: 5

# Test Case 2:
s = "00111"
print(sol.maxScore(s))  # Expected output: 5

# Test Case 3:
s = "1111"
print(sol.maxScore(s))  # Expected output: 3
