# Maximum Number of Removable Characters - LeetCode

## Problem Overview

The problem **Maximum Number of Removable Characters** is a string and binary search problem from LeetCode.

You are given:

* A string `s`.
* A string `p` which is already a **subsequence** of `s`.
* An array `removable` containing indices of `s`.

Your task is to find the **maximum number `k`** such that after removing the first `k` indices from `removable` in string `s`, the string `p` is **still a subsequence** of `s`.

In simple words:
You keep removing characters from `s` using the order given in `removable`, and you want to remove as many as possible while still keeping `p` inside `s` as a subsequence.

---

## What is a Subsequence?

A subsequence means:

* You can delete some characters.
* But the remaining characters must keep their **relative order**.

Example:

```
s = "abcde"
p = "ace"  -> valid subsequence
p = "aec"  -> not a subsequence
```

---

## Example

```
s = "abcacb"
p = "ab"
removable = [3, 1, 0]

Output: 2
```

After removing indices `[3, 1]`, the string becomes:

```
"accb"
```

`"ab"` is still a subsequence.

If we remove `[3, 1, 0]`, it becomes:

```
"ccb"
```

Now `"ab"` is no longer a subsequence.

So the answer is `2`.

---

## Code With Comments

```python
from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        # This function checks whether p is still a subsequence of s
        # after removing certain indices
        def isSubseq(s, subseq, removed):
            i1 = i2 = 0  # pointers for s and p

            while i1 < len(s) and i2 < len(subseq):
                # If current index is removed OR characters do not match
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue

                # Characters match, move both pointers
                i1 += 1
                i2 += 1

            # If we matched all characters of p
            return i2 == len(subseq)

        res = 0
        l, r = 0, len(removable) - 1

        # Binary search on how many characters we can remove
        while l <= r:
            m = (l + r) // 2

            # Take first m+1 indices and mark them as removed
            removed = set(removable[:m + 1])

            # Check if p is still subsequence
            if isSubseq(s, p, removed):
                res = max(res, m + 1)
                l = m + 1  # try removing more
            else:
                r = m - 1  # try removing less

        return res
```

---

## Explanation of the Approach

### Key Insight

As we remove more characters, it becomes **harder** for `p` to remain a subsequence.

So the condition:

> "p is still a subsequence"

is **monotonic**:

* True for small `k`
* Eventually becomes false for larger `k`

This makes the problem perfect for **binary search**.

---

## Step-by-Step Logic

1. We binary search on `k` (how many characters to remove).
2. For a given `k`:

   * Remove the first `k` indices from `removable`.
   * Check if `p` is still a subsequence.
3. If yes → try a bigger `k`.
4. If no → try a smaller `k`.
5. Keep track of the maximum valid `k`.

---

## How `isSubseq` Works

The function uses two pointers:

* One for `s`
* One for `p`

It walks through `s` and tries to match characters of `p` while skipping removed indices.

If all characters of `p` are matched, it returns `True`.

---

## Time and Space Complexity

### Time Complexity

Binary search runs:

```
O(log k)
```

Each check runs:

```
O(n + m)
```

So total:

```
O((n + m) * log k)
```

Where:

* `n` = length of `s`
* `m` = length of `p`
* `k` = length of `removable`

---

### Space Complexity

We store removed indices in a set:

```
O(k)
```

---

## Most Optimal Solution and Why

This solution is optimal because:

* The condition is monotonic, so binary search is the best strategy.
* Any solution must at least scan `s` to verify subsequence.
* Binary search minimizes the number of checks.

You cannot do better than:

```
O((n + m) * log k)
```

because checking subsequence itself takes linear time.

---

## Test Cases
```python
# Test Case 1:
s = "abcacb"
p = "ab"
removable = [3, 1, 0]
solution = Solution()
print(solution.maximumRemovals(s, p, removable))  # Output: 2

# Test Case 2:
s = "abcbddddd"
p = "abcd"
removable = [3, 2, 1, 4, 5, 6]
print(solution.maximumRemovals(s, p, removable))  # Output: 1

# Test Case 3:
s = "abcab"
p = "abc"
removable = [0, 1, 2, 3, 4]
print(solution.maximumRemovals(s, p, removable))  # Output: 0
```