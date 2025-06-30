# Sqrt(x)
# Binary Search Solution:
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m

        return res
    
# TIme Complexity: O(log n) where n is the input number x. The binary search algorithm halves the search space on each iteration, leading to a logarithmic time complexity.
# Space Complexity: O(1) as we are not using any additional data structures.
# The algorithm uses a constant amount of space for variables like l, r, m, and res.
# This is efficient for the problem constraints, which allow x to be as large as 2^31 - 1.


# Test Cases
# Test Case 1:
x = 4
print(Solution().mySqrt(x))  # Output: 2

# Test Case 2:
x = 8
print(Solution().mySqrt(x))  # Output: 2
