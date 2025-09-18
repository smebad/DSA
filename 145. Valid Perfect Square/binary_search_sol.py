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


# Binary Search Solution:
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            if sq > num:
                r = m - 1
            elif sq < num:
                l = m + 1
            else:
                return True

        return False
            
# Time Complexity: O(log n), where n is the input number. This is because we are halving the search space in each iteration of the binary search.
# Space Complexity: O(1), since we are using a constant amount of space for the left, right, and mid variables.
# This binary search solution is more efficient than the brute force solution, especially for larger values of n.


# Test Cases:
sol = Solution()

# Test Case 1:
num = 16
print(sol.isPerfectSquare(num))  # Expected Output: True

# Test Case 2:
num = 14
print(sol.isPerfectSquare(num))  # Expected Output: False