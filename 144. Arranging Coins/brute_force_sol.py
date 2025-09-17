# Arranging Coins
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
