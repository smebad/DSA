# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


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