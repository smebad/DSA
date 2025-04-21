# Best Time to Buy and Sell Stock - LeetCode

## Problem Description
You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i`th day. Your goal is to maximize your profit by choosing a **single day to buy one stock** and choosing a **different day in the future to sell that stock**.

You must buy before you sell, and you can only make **one transaction** (i.e., buy once and sell once).

If no profit can be made, return `0`.

### Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
```

### Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction can be made.
```

### Constraints:
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Brute Force Solution
```python
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
```

### Explanation:
- Loop through every possible pair of buy and sell days.
- Calculate the profit by subtracting buy price from sell price.
- Keep track of the maximum profit.

### Time Complexity:
- **O(n^2)** due to nested loops.

### Space Complexity:
- **O(1)**, no additional space is used except variables.

This approach is inefficient for large arrays and leads to a time limit exceeded (TLE) on platforms like LeetCode.

---

## Optimal Solution (Two Pointers / Sliding Window Approach)
```python
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l = buy day, r = sell day
        maxP = 0     # max profit

        while r < len(prices):
            # If the current price is higher than buying price
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]  # calculate profit
                maxP = max(maxP, profit)       # update max profit
            else:
                l = r  # update buying day to current day
            r += 1    # move to next day

        return maxP
```

### Step-by-Step Explanation:
1. Start with `l = 0` (buying day) and `r = 1` (selling day).
2. If the price at `r` is higher than the price at `l`, calculate the profit.
3. If the price at `r` is lower or equal, move `l` to `r` because it could be a new lower buying price.
4. Always move `r` one step ahead.
5. Keep track of the maximum profit.

### Time Complexity:
- **O(n)**: We only go through the list once.

### Space Complexity:
- **O(1)**: Only a few variables are used.

---

## Summary:
- The brute force approach works but is too slow for large input.
- The optimal approach uses a sliding window technique with two pointers to efficiently track the lowest price and calculate maximum profit.
- This problem teaches a key technique in DSA: how to track min/max values in a single traversal.

---

## Test Cases
```python
# Test Case 1:
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))  # Output: 5

# Test Case 2:
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))  # Output: 0
```
