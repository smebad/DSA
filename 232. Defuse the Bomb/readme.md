# Defuse the Bomb - LeetCode

## Problem Description

The problem **"Defuse the Bomb"** involves decrypting a circular array based on a given key `k`.

You are given:

* A circular integer array `code` of length `n`
* An integer key `k`

Each element in the array must be replaced **simultaneously** according to the following rules:

* If `k > 0`, replace the element at index `i` with the sum of the **next `k` elements**.
* If `k < 0`, replace the element at index `i` with the sum of the **previous `|k|` elements**.
* If `k == 0`, replace every element with `0`.

Because the array is circular:

* The element after the last index wraps to the first index.
* The element before the first index wraps to the last index.

The goal is to return the decrypted array.

---

## Examples

### Example 1

```
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
```

Each element becomes the sum of the next three elements in circular order.

### Example 2

```
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
```

All values become zero when `k` is zero.

### Example 3

```
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
```

Each element becomes the sum of the previous two elements in circular order.

---

## Sliding Window Solution

This problem can be solved efficiently using a **sliding window** while handling circular behavior with modulo operations.

### Code With Comments

```python
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n          # Result array initialized with zeros

        # If k is 0, the answer is already all zeros
        if k == 0:
            return res

        l = 0                 # Left pointer of the sliding window
        curSum = 0            # Current sum of the window

        # Traverse enough elements to cover circular windows
        for r in range(n + abs(k)):
            curSum += code[r % n]   # Add next element using modulo for circular indexing

            # Ensure window size does not exceed |k|
            if r - l + 1 > abs(k):
                curSum -= code[l % n]
                l += 1

            # When window size is exactly |k|, store the sum
            if r - l + 1 == abs(k):
                if k > 0:
                    # Assign sum to the element just before the window
                    res[(l - 1) % n] = curSum
                else:
                    # Assign sum to the element just after the window
                    res[(r + 1) % n] = curSum

        return res
```

---

## Step-by-Step Approach

1. If `k == 0`, return an array of zeros immediately.
2. Use a sliding window of size `|k|`.
3. Move the window over the circular array using modulo indexing.
4. Maintain a running sum of the window.
5. Assign the sum to the correct index depending on whether `k` is positive or negative.

---

## Logic Explained in Simple Words

* You are always summing `|k|` numbers next to the current element.
* Sliding window avoids recomputing sums repeatedly.
* Modulo (`% n`) allows the array to behave like a circle.
* Positive `k` looks forward; negative `k` looks backward.

---

## Time and Space Complexity

### Time Complexity: `O(n)`

* Each element is added and removed from the window at most once.

### Space Complexity: `O(1)`

* Only a few variables are used besides the output array.

---

## Why This Solution Is Optimal

* The problem requires processing all elements at least once.
* Sliding window avoids redundant summation.
* No extra data structures are required.
* This is the most efficient approach possible for this problem.

---

## Test Cases

```python
solution = Solution()
print(solution.decrypt([5,7,1,4], 3))
print(solution.decrypt([1,2,3,4], 0))
print(solution.decrypt([2,4,9,3], -2))
```