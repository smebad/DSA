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


# Brute Force Solution:
class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        while n - row > 0:
            row += 1
            n -= row
        return row
    
# Time Complexity: O(√n), where root(n) is the square root of n and n is the number of coins. This is because the maximum number of complete rows that can be formed with n coins is approximately √(2n), which simplifies to O(√n).
# Space Complexity: O(1), as we are using a constant amount of space regardless of the input size.
# This brute force approach iteratively subtracts the number of coins needed for each row from the total number of coins until there are not enough coins left to complete the next row. The variable `row` keeps track of the number of complete rows formed.


# Test Cases:
sol = Solution()

# Test Case 1
n1 = 5
print(sol.arrangeCoins(n1))  # Output: 2

# Test Case 2
n2 = 8
print(sol.arrangeCoins(n2))  # Output: 3