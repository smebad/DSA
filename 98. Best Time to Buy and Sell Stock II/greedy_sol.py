# Best Time to Buy and Sell Stock II
# Greedy solution:
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
            
        return profit
    
# Time Complexity: O(n), where n is the number of days (length of prices array). This is because we iterate through the prices array once.
# Space Complexity: O(1), as we are using a constant amount of space for the profit variable and the loop index.
# In this greedy solution, we iterate through the prices array once, and we only use a constant amount of space for the profit variable. This solution is efficient for large inputs as it has a time complexity of O(n).


# Test Cases
# Test Case 1:
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices)) # Expected Output: 7

# Test Case 2:
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices)) # Expected Output: 0

# Test Case 3:
prices = [1,2,3,4,5]
print(Solution().maxProfit(prices)) # Expected Output: 4
