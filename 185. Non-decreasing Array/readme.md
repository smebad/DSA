# Non-decreasing Array - LeetCode

## Problem Explanation

The **Non-decreasing Array** problem asks us to determine if we can make a given array non-decreasing by modifying **at most one element**. An array is non-decreasing if each element is **less than or equal to the next one**, meaning `nums[i] <= nums[i + 1]` for every valid index `i`.

### Example 1:

**Input:** `nums = [4, 2, 3]`
**Output:** `true`
**Explanation:** By modifying the first element (4) to 1, we get `[1, 2, 3]`, which is non-decreasing.

### Example 2:

**Input:** `nums = [4, 2, 1]`
**Output:** `false`
**Explanation:** We cannot make this array non-decreasing with only one modification.

### Constraints:

* `1 <= n <= 10^4`
* `-10^5 <= nums[i] <= 10^5`

---

## Code Explanation with Comments

```python
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False  # This flag tracks if we have modified one element already.

        for i in range(len(nums) - 1):
            # If the current pair is in order, move to the next.
            if nums[i] <= nums[i + 1]:
                continue

            # If we already changed one element before, we cannot modify again.
            if changed:
                return False

            # We must decide whether to modify nums[i] or nums[i+1]
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                # Case 1: Modify nums[i] to nums[i+1] (safe to lower the left side)
                nums[i] = nums[i + 1]
            else:
                # Case 2: Modify nums[i+1] to nums[i] (safe to raise the right side)
                nums[i + 1] = nums[i]

            changed = True  # Mark that one modification has been made.

        return True  # If loop finishes, it is possible to make the array non-decreasing.
```

---

## Approach and Logic

This problem is solved using a **Greedy approach**. The main idea is to scan through the array and detect when the non-decreasing property is violated (`nums[i] > nums[i + 1]`). When this happens, we have two possible actions:

1. **Modify the current element (`nums[i]`)** if it does not break the previous order.
2. **Otherwise, modify the next element (`nums[i + 1]`)** to make it larger or equal to `nums[i]`.

We are only allowed **one modification**, so if we detect a second violation, we can immediately return `False`.

This greedy check ensures we make the smallest necessary change to keep the array as consistent as possible without needing multiple passes or sorting.

---

## Why It Works

When we find the first violation (`nums[i] > nums[i + 1]`), the optimal move is to change either the left or right element depending on the surrounding numbers:

* If it’s the first element (`i == 0`), we can safely lower it.
* Otherwise, if `nums[i + 1] >= nums[i - 1]`, lowering `nums[i]` is safe.
* If not, we raise `nums[i + 1]` to `nums[i]`.

This decision ensures that the array stays as close to non-decreasing as possible while using **at most one change**.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)` — We traverse the array once to check and possibly modify elements.
* **Space Complexity:** `O(1)` — We only use a few extra variables, regardless of the input size.

---

## Optimality

This **greedy approach** is the most optimal solution for this problem because:

* It only requires a **single pass** through the array.
* It uses **constant space**.
* It makes decisions locally without needing to recheck the array after modification.

More complex methods (like dynamic programming or backtracking) would be unnecessary and inefficient here.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
print(sol.checkPossibility([4, 2, 3]))  # Expected output: True

# Test Case 2
print(sol.checkPossibility([4, 2, 1]))  # Expected output: False
```