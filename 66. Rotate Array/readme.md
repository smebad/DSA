# Rotate Array - LeetCode

## Problem Description

The **Rotate Array** problem asks you to shift the elements of a given integer array `nums` to the right by `k` steps. Here, `k` is a non-negative integer.

This operation must be done **in-place**, meaning no additional arrays should be used. The rotation should keep the order and structure of the elements intact after the transformation.

### Example 1:

* **Input:** nums = \[1,2,3,4,5,6,7], k = 3
* **Output:** \[5,6,7,1,2,3,4]
* **Explanation:**

  * Step 1: \[7,1,2,3,4,5,6]
  * Step 2: \[6,7,1,2,3,4,5]
  * Step 3: \[5,6,7,1,2,3,4]

### Example 2:

* **Input:** nums = \[-1,-100,3,99], k = 2
* **Output:** \[3,99,-1,-100]

## Constraints

* 1 <= nums.length <= 10^5
* -2^31 <= nums\[i] <= 2^31 - 1
* 0 <= k <= 10^5

## Follow-up

* Try to come up with as many solutions as possible.
* Can you solve it in-place with O(1) extra space?

---

## Solution 1: Reverse Method (Optimal Solution)

```python
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k >= n

        # Helper function to reverse elements in nums from index l to r
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)
```

### How It Works

* First, the whole array is reversed.
* Then, the first `k` elements are reversed again.
* Finally, the rest of the array is reversed.

This gives the effect of rotating the array to the right by `k` steps.

### Time and Space Complexity

* **Time Complexity:** O(n), since we traverse the array three times.
* **Space Complexity:** O(1), because we use only constant extra space.

### Why It's Optimal

* It uses no extra space and runs in linear time.
* Works efficiently even for large values of `n` and `k`.

---

## Solution 2: Brute Force Method

```python
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        while k:
            tmp = nums[n - 1]  # Save the last element
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]  # Shift elements right by 1
            nums[0] = tmp  # Place saved element at the beginning
            k -= 1
```

### How It Works

* Each rotation step shifts all elements by one position to the right.
* This process is repeated `k` times.

### Time and Space Complexity

* **Time Complexity:** O(n \* k), as the array is traversed `k` times.
* **Space Complexity:** O(1), no extra space is used.

### When to Use

* Only suitable for small arrays or small values of `k`.
* Becomes inefficient for large inputs due to quadratic time complexity.

---

## Summary of Differences

| Feature          | Reverse Method  | Brute Force       |
| ---------------- | --------------- | ----------------- |
| Time Complexity  | O(n)            | O(n \* k)         |
| Space Complexity | O(1)            | O(1)              |
| In-place         | Yes             | Yes               |
| Efficiency       | High (Optimal)  | Low (Inefficient) |
| Suitable for     | All input sizes | Small inputs only |

---

## Test Cases

```python
# Test Case 1
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)  # Output: [5,6,7,1,2,3,4]

# Test Case 2
nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
print(nums)  # Output: [3,99,-1,-100]
```
