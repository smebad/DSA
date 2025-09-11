# Set Mismatch - LeetCode

## Problem Explanation

The **Set Mismatch** problem is about finding two specific numbers in a corrupted set. Originally, the set contains all integers from 1 to *n*. However, due to an error:

* One number appears **twice** (duplicate).
* One number is **missing**.

You are given an integer array `nums` that represents this corrupted set. The task is to return the duplicate number and the missing number in the form `[duplicate, missing]`.

### Example

* Input: `nums = [1, 2, 2, 4]`

* Output: `[2, 3]`

* Explanation: The number `2` is duplicated, and the number `3` is missing.

* Input: `nums = [1, 1]`

* Output: `[1, 2]`

## Code with Comments

```python
from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]  # res[0] will store duplicate, res[1] will store missing
        count = Counter(nums)  # Count frequency of each number in nums

        # Iterate through numbers from 1 to n
        for i in range(1, len(nums) + 1):
            if count[i] == 0:   # If a number never appears, it is missing
                res[1] = i
            if count[i] == 2:   # If a number appears twice, it is the duplicate
                res[0] = i

        return res
```

## Solution Approach

The idea behind this solution is simple:

1. Use a **hash table (Counter)** to count how many times each number appears.
2. Loop through all numbers from `1` to `n`.

   * If a number never appears (`count[i] == 0`), that number is **missing**.
   * If a number appears twice (`count[i] == 2`), that number is the **duplicate**.
3. Return both numbers.

### Why this works

* Since the array should have contained exactly one copy of every number from `1` to `n`, any deviation will mean:

  * One number is repeated.
  * One number is skipped.

## Complexity Analysis

* **Time Complexity**: O(n)

  * Counting frequencies takes O(n).
  * Iterating from 1 to n also takes O(n).
  * Total: O(n).
* **Space Complexity**: O(n) in the worst case.

  * The `Counter` stores counts for up to `n` numbers.

## Test Cases

```python
sol = Solution()

# Test Case 1
nums = [1, 2, 2, 4]
print(sol.findErrorNums(nums))  # Output: [2, 3]

# Test Case 2
nums = [1, 1]
print(sol.findErrorNums(nums))  # Output: [1, 2]
```