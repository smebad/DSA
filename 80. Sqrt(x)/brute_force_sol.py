# Sqrt(x)
# Brute Force Solution:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        res = 1
        for i in range(1, x + 1):
            if i * i > x:
                return res
            res = i

        return res
    
# TIme Complexity: O(sqrt(n)), where n is the input number x. The loop iterates from 1 to x, checking each integer to see if its square exceeds x.
# Space Complexity: O(1), as we are using a constant amount of space for the variable `res` and the loop index `i`. No additional data structures are used.
# This brute force solution is straightforward but not efficient for large values of x, as it checks every integer up to x. For larger inputs, more efficient methods like binary search or recursion are preferred.


# Test Cases
# Test Case 1:
x = 4
print(Solution().mySqrt(x))  # Output: 2

# Test Case 2:
x = 8
print(Solution().mySqrt(x))  # Output: 2
