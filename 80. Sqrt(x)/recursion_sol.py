# Sqrt(x)
# Recursion Solution:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = self.mySqrt(x >> 2) << 1
        r = l + 1
        return l if r ** 2 > x else r
    
# TIme Complexity: O(log n) where n is the input number x. The recursion effectively reduces the problem size by a factor of 4 on each call, leading to logarithmic time complexity.
# Space Complexity: O(log n) due to the recursion stack. Each recursive call adds a
# frame to the call stack, and the maximum depth of recursion is logarithmic in relation to x.
# This recursion solution is efficient for the problem constraints, which allow x to be as large as 2^31 - 1.


# Test Cases
# Test Case 1:
x = 4
print(Solution().mySqrt(x))  # Output: 2

# Test Case 2:
x = 8
print(Solution().mySqrt(x))  # Output: 2
