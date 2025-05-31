# Kth Largest Element in an Array - LeetCode

## Problem Statement

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

Note: It is the kth largest element **in sorted order**, **not** the kth distinct element.

You are also asked to solve it **without full sorting** if possible.

---

## Examples

### Example 1:

**Input:** `nums = [3,2,1,5,6,4]`, `k = 2`
**Output:** `5`

### Example 2:

**Input:** `nums = [3,2,3,1,2,4,5,5,6]`, `k = 4`
**Output:** `4`

---

## Constraints

* `1 <= k <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`

---

## Solution 1: Sorting Approach

```python
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order
        return nums[len(nums) - k]  # Return the kth largest by indexing from the end
```

### Code Explanation:

* The array is sorted in ascending order.
* The kth largest element is at index `len(nums) - k`.

### Time and Space Complexity:

* **Time Complexity:** `O(n log n)` due to the sorting step.
* **Space Complexity:** Depends on sorting algorithm. In Python, built-in `sort()` uses Timsort:

  * Worst-case space: `O(n)`
  * Best-case space: `O(1)`

### Pros and Cons:

* Simple and easy to implement.
* Not optimal if the array is large and `k` is small because it sorts the entire array.

---

## Solution 2: Min-Heap (Heapq)

```python
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]  # Get the k largest elements and return the last one
```

### Code Explanation:

* `heapq.nlargest(k, nums)` returns a list of the k largest elements in descending order.
* We return the last element in this list, which is the kth largest.

### Time and Space Complexity:

* **Time Complexity:** `O(n log k)`

  * Building a heap of size `k` and inserting all `n` elements into it.
* **Space Complexity:** `O(k)`

  * For storing the heap of size `k`.

### Pros and Cons:

* More efficient than full sorting when `k` is small compared to `n`.
* Still uses extra space for the heap.

---

## Which One is Optimal?

The **Min-Heap solution** is the optimal one in terms of time efficiency when `k` is small relative to the size of the array:

* It avoids sorting the entire array.
* It uses a data structure that helps keep only the `k` largest elements.
* Better suited for large datasets with small `k`.

Sorting is easier to implement but is not optimal in time complexity.

---

## Summary

* **Sorting** is straightforward but less efficient.
* **Heap** helps improve performance by focusing only on the necessary `k` elements.
* Use sorting for simplicity and debugging.
* Use a heap for better performance in interviews and real applications.

---

## Test Cases

```python
# Test Case 1:
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))  # Output: 5

# Test Case 2:
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution().findKthLargest(nums, k))  # Output: 4
```

---

This problem is a great example of how different data structures (like heaps) can make solutions more efficient compared to brute-force approaches like sorting.
