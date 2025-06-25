# Online Stock Span - LeetCode

## Problem Description

The **Online Stock Span** problem involves designing a data structure that keeps track of stock prices and efficiently computes the "span" of the current day's price. The **span** is defined as the number of consecutive days (including today) the stock price was less than or equal to today's price.

**Methods to Implement:**

* `StockSpanner()`: Initializes the object.
* `next(price)`: Returns the span of the given stock price for today.

**Example:**

```
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output:
[null, 1, 1, 1, 2, 1, 4, 6]
```

---

## Monotonic Stack Solution

```python
from typing import List

class StockSpanner:

    def __init__(self):
        self.stack = []  # Each element is a pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        # Merge spans of previous prices less than or equal to current
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]  # Accumulate the span
            self.stack.pop()  # Remove the lower or equal price
        self.stack.append((price, span))  # Push current price with span
        return span
```

---

## Code Explanation

* We use a **monotonic decreasing stack** to store pairs of `(price, span)`.
* On each call to `next(price)`:

  * We initialize `span = 1` for the current day.
  * While the top of the stack has a price less than or equal to the current price:

    * We add its span to `span` (accumulate consecutive span).
    * Pop that price from the stack.
  * Finally, push the current `(price, span)` onto the stack.

---

## Approach and Logic

* The algorithm efficiently avoids rechecking earlier prices by storing precomputed spans.
* The use of a monotonic decreasing stack ensures:

  * Prices are ordered from highest to lowest.
  * When a higher or equal price is found, all lower or equal prices (and their spans) are combined.
* This allows us to calculate spans in **amortized constant time**.

**Why it works:**

* Each price is pushed and popped at most once.
* Therefore, for `n` calls, we perform at most `2n` stack operations.

---

## Time and Space Complexity

* **Time Complexity:** O(n), where `n` is the number of calls to `next()`. Each price is added and removed at most once.
* **Space Complexity:** O(n), for storing the stack of prices and their spans.

**Why this is optimal:**

* The approach ensures minimal stack operations.
* No nested loops or repeated checks beyond necessary conditions.

---

## Test Cases

```python
# Test Case 1
stock_spanner1 = StockSpanner()
print(stock_spanner1.next(100))  # Output: 1
print(stock_spanner1.next(80))   # Output: 1
print(stock_spanner1.next(60))   # Output: 1
print(stock_spanner1.next(70))   # Output: 2
print(stock_spanner1.next(60))   # Output: 1
print(stock_spanner1.next(75))   # Output: 4
print(stock_spanner1.next(85))   # Output: 6
```
