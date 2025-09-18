# Valid Perfect Square
# Brute Force Solution:

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            sq = i * i
            if sq > num:
                return False
            if sq == num:
                return True
            
# Time Complexity: O(√n), where square root of n is the number of iterations we are doing. This is because we are iterating through the square root of n.
# Space Complexity: O(1), since we are using a constant amount of space for the result variable.
# This brute force solution works well for small values of n, but it can be inefficient for larger values of n.


# Test Cases:
sol = Solution()

# Test Case 1:
num = 16
print(sol.isPerfectSquare(num))  # Expected Output: True

# Test Case 2:
num = 14
print(sol.isPerfectSquare(num))  # Expected Output: False
