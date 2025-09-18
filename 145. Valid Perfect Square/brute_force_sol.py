# Valid Perfect Square
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

# Constraints:

# 1 <= num <= 231 - 1


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