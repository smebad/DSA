# Random Pick with Weight - LeetCode

## Problem Overview

The problem **Random Pick with Weight** is a probability and prefix sum problem from LeetCode.

You are given:

* An array `w` where each `w[i]` represents the **weight** of index `i`.

You need to implement a function `pickIndex()` that:

* Randomly returns an index between `0` and `len(w) - 1`.
* The probability of picking index `i` should be:

```
w[i] / sum(w)
```

This means that indices with higher weights should be picked more frequently.

---

## Intuition Behind the Problem

Think of the weights as lengths on a number line.

Example:

```
w = [1, 3]
```

This represents the range:

```
[0, 1) -> index 0
[1, 4) -> index 1
```

If we randomly pick a number between `0` and `4`, then:

* Numbers in `[0,1)` map to index `0`
* Numbers in `[1,4)` map to index `1`

So index `1` is three times more likely to be chosen.

---

## Binary Search Solution (Code With Comments)

```python
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        # Build prefix sum array
        # prefix[i] will store sum of weights up to index i-1
        self.prefix = [0]
        for wgt in w:
            self.prefix.append(self.prefix[-1] + wgt)

    def pickIndex(self) -> int:
        # Generate a random number between 0 and total weight
        target = self.prefix[-1] * random.random()

        # Binary search to find smallest index such that
        # prefix[index] > target
        l, r = 1, len(self.prefix)

        while l < r:
            mid = (l + r) >> 1

            if self.prefix[mid] <= target:
                l = mid + 1
            else:
                r = mid

        # Subtract 1 because prefix array has extra 0 at start
        return l - 1
```

---

## Step-by-Step Approach

### Step 1: Build Prefix Sum Array

We convert the weight array into a prefix sum array.

Example:

```
w = [1, 3, 2]
prefix = [0, 1, 4, 6]
```

Each index now represents a range on the number line:

* Index 0: [0,1)
* Index 1: [1,4)
* Index 2: [4,6)

---

### Step 2: Generate a Random Number

We generate a random float between:

```
0 and total_weight
```

This ensures uniform probability over the entire range.

---

### Step 3: Binary Search

We find the **first prefix sum that is greater than the random number**.

That index is the selected index.

This is the key idea that maps probability to actual indices.

---

## Why Binary Search Works Here

Because the prefix array is:

* Sorted
* Increasing

We can use binary search to find the correct bucket in:

```
O(log n)
```

---

## Time and Space Complexity

### Time Complexity

Initialization:

```
O(n)
```

Each call to `pickIndex()`:

```
O(log n)
```

---

### Space Complexity

Prefix array storage:

```
O(n)
```

---

## Most Optimal Solution and Why

The prefix sum + binary search approach is optimal because:

* We must preprocess at least once to store probabilities.
* Each random pick must at least locate a range.
* Binary search is the fastest possible way to do this.

You cannot do better than:

```
O(log n)
```

per query without using advanced data structures.

