# Online Stock Span
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
