# Online Stock Span
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
 

# Example 1:

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
 

# Constraints:

# 1 <= price <= 105
# At most 104 calls will be made to next.


# Monotonic Decreasing Stack Solution:
from typing import List

class StockSpanner:

    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
    
# Time Complexity: O(n) where n is the number of calls to next. Each price is pushed and popped from the stack at most once.
# Space Complexity: O(n) in the worst case where all prices are stored in the stack.
# What is Monotonic Decreasing Stack? A stack where the elements are in non-increasing order.
# This solution uses a monotonic decreasing stack to efficiently calculate the span of stock prices. The stack stores pairs of (price, span), allowing us to quickly determine how many consecutive days the price was less than or equal to the current day's price.
# However this stack solution is efficient for calculating the stock span, it does not handle the case where the stock price is equal to the previous day's price. In such cases, the span should include the previous day's span as well. The current implementation does not account for this, so it may return incorrect spans in those scenarios.


# Test cases
# Test Case 1:
stock_spanner1 = StockSpanner()
print(stock_spanner1.next(100))  # Output: 1
print(stock_spanner1.next(80))   # Output: 1
print(stock_spanner1.next(60))   # Output: 1
print(stock_spanner1.next(70))   # Output: 2
print(stock_spanner1.next(60))   # Output: 1
print(stock_spanner1.next(75))   # Output: 4
print(stock_spanner1.next(85))   # Output: 6