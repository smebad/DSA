# Best Time to Buy and Sell Stock II - LeetCode

## Problem Explanation

The "Best Time to Buy and Sell Stock II" problem is a common algorithmic problem focused on finding the maximum profit from stock prices over a number of days. You're given a list where each element represents the price of a stock on a specific day.

You are allowed to buy and/or sell the stock on any day, and you may execute as many transactions as you like (buy one and sell one share of the stock multiple times). However, you can only hold at most one share of the stock at a time, and you can buy and sell on the same day.

Your goal is to determine the maximum profit that can be achieved.

### Examples:

* **Input**: `[7,1,5,3,6,4]`
  **Output**: `7`
  **Explanation**: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 3. Total profit = 7.

* **Input**: `[1,2,3,4,5]`
  **Output**: `4`
  **Explanation**: Buy on day 1 and sell on day 5.

* **Input**: `[7,6,4,3,1]`
  **Output**: `0`
  **Explanation**: Prices are continuously decreasing, so no transactions are done.

## Code Explanation

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # Loop through prices from the second day to the last day
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's, buy yesterday and sell today
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
                # This effectively captures every upward trend
        
        return profit
```

### Comments for Understanding:

* We initialize `profit` to zero.
* We iterate through the array from index 1.
* Whenever the current price is greater than the previous day, we add the difference to `profit`.
* This simulates buying at the lowest point before each rise and selling at the peak.

## Solution Approach and Logic

This is a **greedy solution**. The key observation is that we don't need to find local minima or maxima explicitly. Instead, we simply add up all the small profits made from every increase in price.

In simple words:

* If the price goes up compared to the previous day, we treat it as a buy-sell opportunity and accumulate that profit.
* This is valid because we can sell and buy again on the same day, and we are allowed multiple transactions.

This solution avoids unnecessary complexity and works efficiently with the given constraints.

### Why is this Optimal?

* It looks for **every opportunity to make a profit** without waiting for the entire valley-to-peak pattern.
* This greedy strategy ensures no potential gain is missed.

## Time and Space Complexity

* **Time Complexity**: `O(n)`, where `n` is the number of days (length of the prices array). We traverse the array once.
* **Space Complexity**: `O(1)`, since we only use a constant amount of space (the `profit` variable).

This is the most optimal solution because:

* It only requires a single pass through the data.
* It does not use any additional memory.
* It maximizes the profit by taking advantage of all upward trends.

## Test Cases

```python
# Test Case 1:
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))  # Expected Output: 7

# Test Case 2:
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))  # Expected Output: 0

# Test Case 3:
prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))  # Expected Output: 4
```
