# Valid Perfect Square
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
