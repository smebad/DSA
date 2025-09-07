# Minimum Changes To Make Alternating Binary String
# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

 

# Example 1:

# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:

# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:

# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
 

# Constraints:

# 1 <= s.length <= 104
# s[i] is either '0' or '1'.


# Start with Zero or One Solution:
class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            if i % 2 == 0:
                count += 1 if s[i] == '0' else 0
            else:
                count += 1 if s[i] == '1' else 0

        return min(count, len(s) - count)
    
# Time Complexity: O(n), where n is the length of the string s. We iterate through the string once to count the number of changes needed.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This solution efficiently counts the number of changes needed to convert the string into an alternating binary string starting with '0' and '1', and returns the minimum of the two counts. The solution is optimal for the given problem constraints.


# Test Cases
sol = Solution()

# Test Case 1:
s = "0100"
print(sol.minOperations(s))  # Expected output: 1

# Test Case 2:
s = "10"
print(sol.minOperations(s))  # Expected output: 0

# Test Case 3:
s = "1111"
print(sol.minOperations(s))  # Expected output: 2