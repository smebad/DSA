# Minimum Changes To Make Alternating Binary String
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
