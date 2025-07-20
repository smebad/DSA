# Sort an Array - LeetCode

## Problem Description

**Sort an Array** is a classic algorithm problem where you're given an array of integers, and the task is to sort it in ascending order **without using any built-in sorting functions**. Moreover, the solution must be efficient with a time complexity of **O(n log n)** and use the **smallest possible space**.

### Problem Constraints:

* `1 <= nums.length <= 50,000`
* `-50,000 <= nums[i] <= 50,000`

### Example:

**Input:** `[5,2,3,1]`
**Output:** `[1,2,3,5]`

**Input:** `[5,1,1,2,0,0]`
**Output:** `[0,0,1,1,2,5]`

---

## Merge Sort Solution

Merge Sort is a **divide-and-conquer** algorithm that splits the array into halves recursively, sorts each half, and merges them back together in sorted order.

```python
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            # Create left and right subarrays
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            # Merge the two sorted halves into the original array
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            # Copy any remaining elements from left half
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1

            # Copy any remaining elements from right half
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
```

### Merge Sort Analysis:

* **Time Complexity:** O(n log n) because the array is split in half recursively and merged back.
* **Space Complexity:** O(n) due to temporary subarrays used during merging.
* **Best Use Case:** When stable sorting is required, and space is not a major constraint.

---

## Heap Sort Solution

Heap Sort builds a **max-heap** from the array and then repeatedly extracts the maximum element (root of heap), placing it at the end of the array.

```python
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums

    def heapify(self, arr, n, i):
        # Initialize left, right children and assume i is largest
        l = (i << 1) + 1
        r = (i << 1) + 2
        largest = i

        # Compare left child
        if l < n and arr[l] > arr[largest]:
            largest = l

        # Compare right child
        if r < n and arr[r] > arr[largest]:
            largest = r

        # If a larger child was found, swap and recurse
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Move max to end
            self.heapify(arr, i, 0)
```

### Heap Sort Analysis:

* **Time Complexity:** O(n log n), due to building the heap and repeated heapify operations.
* **Space Complexity:** O(log n) due to recursion stack used in heapify.
* **Best Use Case:** When in-place sorting is critical and you want to minimize space usage.

---

## Comparison and Conclusion

| Algorithm  | Time Complexity | Space Complexity | Stability | In-place |
| ---------- | --------------- | ---------------- | --------- | -------- |
| Merge Sort | O(n log n)      | O(n)             | Yes       | No       |
| Heap Sort  | O(n log n)      | O(log n)         | No        | Yes      |

* **Merge Sort** is more readable and stable but uses more space.
* **Heap Sort** is more memory efficient and sorts in-place but is not stable.

### Optimal Solution:

* If stability and simplicity are important, **Merge Sort** is preferable.
* If minimizing space is the goal and stability isn't required, **Heap Sort** is the optimal choice due to its in-place nature and better space complexity.

Both solutions respect the O(n log n) time constraint and are excellent for large datasets where built-in functions are restricted.