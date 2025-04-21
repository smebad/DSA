# Best Time to Buy and Sell Stock
# Brute force solution:
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res
    
# Time complexity: O(n^2) where n is the length of prices.
# Space complexity: O(1) as we are using only a constant amount of space.
# This brute force solution is not efficient for large inputs as it has a time complexity of O(n^2). It is not optimal and can be improved to O(n) time complexity using a two pointers (Sliding Window) approach.


# Test Cases:
# Test Case 1:
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices)) # Expected Output: 5

# Test Case 2:
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices)) # Expected Output: 0
