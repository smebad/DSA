# Arranging Coins
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1


# Binary Search Solution:
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid * (mid + 1)) // 2
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)

        return res
# Time Complexity: O(log n), where n is the number of coins. This is because we are using binary search to find the maximum number of complete rows, which reduces the search space by half in each iteration.
# Space Complexity: O(1), as we are using a constant amount of space regardless of the input size.
# This binary search approach is efficiently narrows down the possible number of complete rows by calculating the total number of coins needed for a given number of rows (using the formula k(k + 1)/2) and adjusting the search range based on whether the calculated coins exceed the available coins n.



# Test Cases:
sol = Solution()

# Test Case 1
n1 = 5
print(sol.arrangeCoins(n1))  # Output: 2

# Test Case 2
n2 = 8
print(sol.arrangeCoins(n2))  # Output: 3