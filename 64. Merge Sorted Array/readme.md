# Merge Sorted Array - LeetCode

## Problem Description

The **Merge Sorted Array** problem involves combining two sorted integer arrays, `nums1` and `nums2`, into one sorted array in non decreasing order. The twist is that the final result must be stored in-place within `nums1`.

`nums1` has a length of `m + n`, where the first `m` elements are valid and the remaining `n` elements are placeholders (zeros) for the merge. `nums2` contains `n` valid elements.

### Example 1:

* **Input:** `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`
* **Output:** `[1,2,2,3,5,6]`

### Example 2:

* **Input:** `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
* **Output:** `[1]`

### Example 3:

* **Input:** `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`
* **Output:** `[1]`

## Constraints

* `nums1.length == m + n`
* `nums2.length == n`
* `0 <= m, n <= 200`
* `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Follow-up

Can you come up with an algorithm that runs in **O(m + n)** time?

---

## Solution 1: Three Pointers (Optimal Solution)

```python
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Modify nums1 in-place to store the merged sorted array.
        """
        last = m + n - 1  # Index of last position in nums1

        # Traverse from the end of nums1 and nums2
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]  # Place the larger value at the end
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # If any elements are left in nums2, place them
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
```

### Explanation

* We start merging from the end to avoid overwriting the initial values in `nums1`.
* We compare the largest remaining elements from `nums1` and `nums2`, placing the larger at the end.
* Once one of the arrays is exhausted, we fill in the rest of the values from `nums2` if needed.

### Time Complexity

* **O(m + n)**: We traverse both arrays once.

### Space Complexity

* **O(1)**: In-place merge without extra data structures.

### Why It's Optimal

* Uses no extra memory and achieves linear runtime.
* Efficient even for larger inputs.

---

## Solution 2: Sorting Based Solution

```python
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Modify nums1 in-place by copying and sorting.
        """
        nums1[m:] = nums2[:n]  # Copy nums2 into the empty space of nums1
        nums1.sort()           # Sort the entire array
```

### Explanation

* Replace the empty positions in `nums1` with elements from `nums2`.
* Then sort the whole array to get the final result.

### Time Complexity

* **O((m + n) log(m + n))**: Due to the sorting step.

### Space Complexity

* **O(1)** or **O(m + n)** depending on sorting implementation.

### When to Use

* Simple to implement, but less efficient for large arrays compared to the three-pointer method.

---

## Summary of Differences

| Feature          | Three Pointers | Sorting-Based         |
| ---------------- | -------------- | --------------------- |
| Time Complexity  | O(m + n)       | O((m + n) log(m + n)) |
| Space Complexity | O(1)           | O(1) or O(m + n)      |
| In-Place         | Yes            | Yes                   |
| Speed            | Faster         | Slower                |
| Simplicity       | Moderate       | Easiest               |

---

## Test Cases

```python
# Test Case 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

# Test Case 2
nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

# Test Case 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]
```

---

## Final Notes

* The three pointer approach is the most efficient and optimal solution for merging sorted arrays in-place.
* Understanding how to manipulate array indices is key for solving in place problems like this.
