# Sort Array by Increasing Frequency - LeetCode

## Problem Explanation

The problem **"Sort Array by Increasing Frequency"** asks us to reorder an integer array `nums` such that:

1. Numbers with lower frequency (appear fewer times) come first.
2. If multiple numbers have the same frequency, they should be sorted in **decreasing order by value**.

We must return the rearranged array according to these rules.

### Example

* **Input:** `nums = [1,1,2,2,2,3]`
  **Output:** `[3,1,1,2,2,2]`
  Explanation: `3` appears once, `1` appears twice, `2` appears three times.

* **Input:** `nums = [2,3,1,3,2]`
  **Output:** `[1,3,3,2,2]`
  Explanation: Both `2` and `3` appear twice, so the one with the larger value (`3`) comes first.

* **Input:** `nums = [-1,1,-6,4,5,-6,1,4,1]`
  **Output:** `[5,-1,4,4,-6,-6,1,1,1]`

---

## Code Explanation

```python
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each number using Counter
        count = Counter(nums)

        # Step 2: Sort the array with a custom key
        # The key is a tuple: (frequency of number, -value of number)
        # - Numbers with lower frequency come first
        # - If frequencies are equal, the larger number (-n makes it descending) comes first
        nums.sort(key=lambda n: (count[n], -n))

        return nums
```

### Walkthrough of Code

1. **`Counter(nums)`** counts how many times each number appears in the list.
2. **Sorting key `(count[n], -n)`**:

   * `count[n]`: ensures sorting is based on frequency (ascending).
   * `-n`: ensures that when frequencies are equal, larger numbers come first.
3. Finally, return the sorted list.

---

## Approach and Logic

* First, we count frequencies of all numbers.
* Then we sort the numbers using a **custom sorting rule**:

  1. Numbers with lower frequency first.
  2. If two numbers have the same frequency, the higher number comes first.
* The sorting is handled in **one pass** by Python’s efficient `sort` function.

---

## Complexity Analysis

* **Time Complexity:** `O(n log n)`

  * Counting frequencies with `Counter` takes `O(n)`.
  * Sorting takes `O(n log n)`.
  * The sorting step dominates the runtime.

* **Space Complexity:** `O(n)`

  * Extra space is needed for the `Counter` dictionary storing frequencies.

---

## Test Cases

```python
sol = Solution()

# Test Case 1:
nums1 = [1,1,2,2,2,3]
print(sol.frequencySort(nums1))  # Output: [3,1,1,2,2,2]

# Test Case 2:
nums2 = [2,3,1,3,2]
print(sol.frequencySort(nums2))  # Output: [1,3,3,2,2]

# Test Case 3:
nums3 = [-1,1,-6,4,5,-6,1,4,1]
print(sol.frequencySort(nums3))  # Output: [5,-1,4,4,-6,-6,1,1,1]
```