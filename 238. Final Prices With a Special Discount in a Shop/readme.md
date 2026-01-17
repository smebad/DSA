# Final Prices With a Special Discount in a Shop - LeetCode

## 1. Problem Explanation

**Final Prices With a Special Discount in a Shop** is a classic stack-based problem that focuses on finding the next smaller or equal element to the right.

You are given an array `prices`, where `prices[i]` represents the price of the `i`th item in a shop.

### Discount Rule

For each item `i`:

* You receive a discount equal to `prices[j]`, where `j` is the **smallest index greater than `i`** such that:

  `prices[j] <= prices[i]`

* If no such `j` exists, no discount is applied.

The final price of item `i` becomes:

```
prices[i] - prices[j]
```

If no discount is found, the price remains the same.

### Goal

Return an array `answer` where `answer[i]` is the final price after applying the special discount rule.

---

## 2. Code With Comments
```python
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Copy original prices to result array
        # We will subtract discounts directly from this
        res = [p for p in prices]

        # Stack will store indices of items
        # These are items waiting to find their discount
        stack = []

        # Traverse through each price
        for i in range(len(prices)):
            # While there is an item in the stack and
            # current price is less than or equal to the price
            # at the top index of the stack
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()        # Index that gets the discount
                res[j] -= prices[i]   # Apply discount

            # Push current index onto the stack
            stack.append(i)

        return res
```

---

## 3. Solution Approach and Logic

### Key Insight

For each item, we need to find the **first cheaper or equal item to its right**.

This is a classic **Next Smaller Element** problem, which is best solved using a **monotonic stack**.

---

### Stack-Based Approach

We use a **monotonic increasing stack** that stores indices of items whose discount is not yet found.

#### Step-by-Step Logic

1. Traverse prices from left to right
2. Maintain a stack of indices where prices are in increasing order
3. When a smaller or equal price is found:

   * Pop indices from the stack
   * Apply the discount using the current price
4. Push the current index into the stack
5. Items left in the stack receive no discount

---

### Why This Works

* Each index is pushed once
* Each index is popped once
* The first smaller or equal element is guaranteed by the stack order

---

## 4. Time and Space Complexity

### Time Complexity

```
O(n)
```

* Each element is pushed and popped at most once
* Single pass through the array

### Space Complexity

```
O(n)
```

* Stack can contain up to `n` indices in the worst case
* Result array also uses `O(n)` space

---

## Why This Is the Most Optimal Solution

* Brute force checks every pair of elements (`O(n²)`)
* Stack solution processes each element only once
* Efficient even for the maximum constraints

This makes the stack-based solution the best possible approach for this problem.

---

## Example Walkthrough

Input:

```
prices = [8, 4, 6, 2, 3]
```

Processing:

* 8 gets discount 4
* 4 gets discount 2
* 6 gets discount 2
* 2 has no discount
* 3 has no discount

Output:

```
[4, 2, 4, 2, 3]
```

---

## Test Cases

```python
# Test Case 1
prices = [8, 4, 6, 2, 3]
print(Solution().finalPrices(prices))

# Test Case 2
prices = [1, 2, 3, 4, 5]
print(Solution().finalPrices(prices))

# Test Case 3
prices = [10, 1, 1, 6]
print(Solution().finalPrices(prices))
```