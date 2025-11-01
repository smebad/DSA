# Largest Number - LeetCode

## 1. Problem Explanation

The **Largest Number** problem asks us to arrange a list of non-negative integers in such an order that when we concatenate them, they form the largest possible number. Since the result can be very large, we return it as a string instead of a numeric value.

### Key Idea

When deciding the order between two numbers, say `a` and `b`, we do not compare them normally. Instead, we compare the concatenated results:

* `a + b`
* `b + a`

Whichever concatenation gives a larger number should come first.

### Example

Input: `[3, 30, 34, 5, 9]`
Possible order that gives the largest number: `9 5 34 3 30`
Output: `"9534330"`

## 2. Code With Explanation

```python
from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings so we can concatenate them
        for i, num in enumerate(nums):
            nums[i] = str(num)

        # Custom comparator to decide which string should come first
        def compare(n1, n2):
            # If n1+n2 forms a bigger number, n1 should come first
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        # Sort using the custom comparator
        nums = sorted(nums, key=cmp_to_key(compare))

        # Join the numbers. Use int() to handle cases like [0,0] => "0"
        return str(int("".join(nums)))
```

## 3. Approach and Logic

### Concept

* Instead of sorting numbers traditionally, sort based on the best concatenation order.
* Compare `a+b` and `b+a` as strings.
* Example: Compare `9` and `34`:

  * `934 > 349` so `9` should come before `34`.

### Why this works

Lexicographically comparing concatenated strings ensures the sequence builds the maximum possible number.

### Handling Special Case

If all numbers are zero (e.g., `[0,0]`), concatenation would produce `"00"`. Converting to `int` and back to `str` gives `"0"`.

## 4. Time & Space Complexity

| Complexity           | Explanation                                  |
| -------------------- | -------------------------------------------- |
| **Time: O(n log n)** | Sorting dominates the time complexity        |
| **Space: O(n)**      | Need to store string versions of all numbers |

### Why this is optimal

* We must inspect and compare elements to know their optimal order, so sorting (`O(n log n)`) is the most efficient strategy.
* Custom comparison guarantees the largest string concatenation outcome.

## 5. Test Cases

```python
sol = Solution()

print(sol.largestNumber([10, 2]))        # "210"
print(sol.largestNumber([3, 30, 34, 5, 9]))  # "9534330"
print(sol.largestNumber([0, 0]))         # "0"
```
