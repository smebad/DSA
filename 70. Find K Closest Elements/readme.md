# Find K Closest Elements - LeetCode

## Problem Description

The **Find K Closest Elements** problem asks us to return the `k` closest integers to a target value `x` from a sorted array `arr`. The output must also be in ascending order.

An integer `a` is closer to `x` than integer `b` if:

* `|a - x| < |b - x|`, or
* `|a - x| == |b - x|` and `a < b`

### Example 1:

* Input: `arr = [1,2,3,4,5]`, `k = 4`, `x = 3`
* Output: `[1,2,3,4]`

### Example 2:

* Input: `arr = [1,1,2,3,4,5]`, `k = 4`, `x = -1`
* Output: `[1,1,2,3]`

### Constraints:

* `1 <= k <= arr.length`
* `1 <= arr.length <= 10^4`
* `arr` is sorted in ascending order.
* `-10^4 <= arr[i], x <= 10^4`

---

## Binary Search Solution

```python
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k  # define binary search boundaries
        while l < r:
            m = (l + r) // 2  # calculate mid index
            # check if the left side is further from x than the right side
            if x - arr[m] > arr[m + k] - x:
                l = m + 1  # move window to the right
            else:
                r = m  # keep or move window to the left
        return arr[l:l + k]  # return the subarray starting from the correct index
```

### Explanation of Code

* Binary search is used to find the starting point of the window of `k` elements.
* The condition `x - arr[m] > arr[m + k] - x` determines if the current left window is further from `x` than the next possible one.
* The loop narrows down until `l` is the starting index for the closest `k` elements.

---

## Two Pointers Solution

```python
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        # shrink the window until it contains exactly k elements
        while r - l >= k:
            # if the left element is closer or equally close, remove rightmost
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l: r + 1]  # return k closest elements
```

### Explanation of Code

* This approach uses a shrinking window between `l` and `r`.
* We eliminate the farther of the two ends based on proximity to `x`.
* Once `r - l + 1 == k`, we return the subarray.

---

## Approach and Logic

Both methods use the fact that the input array is **sorted**:

### Binary Search:

* Uses binary search to find the left boundary of a window of size `k`.
* Optimal for finding the subarray directly.

### Two Pointers:

* Shrinks the window from both sides until exactly `k` closest elements remain.
* Simpler to understand, but a bit slower than binary search in practice.

---

## Time and Space Complexities

### Binary Search:

* **Time Complexity:** `O(log(n - k))`
* **Space Complexity:** `O(k)` for the result list

### Two Pointers:

* **Time Complexity:** `O(n - k)`
* **Space Complexity:** `O(k)` for the result list

### Which is Optimal?

* **Binary search** is more efficient, especially when `k` is small compared to `n`, since the number of iterations is based on a logarithmic search range.

---

## Test Cases

```python
# Test Case 1:
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(Solution().findClosestElements(arr, k, x))  # Output: [1, 2, 3, 4]

# Test Case 2:
arr = [1, 1, 2, 3, 4, 5]
k = 4
x = -1
print(Solution().findClosestElements(arr, k, x))  # Output: [1, 1, 2, 3]
```

---

## Final Notes

* Both solutions use properties of a sorted array for efficient searching.
* Binary search is slightly more complex but faster.
* Two pointers is easier to grasp for beginners.
* Both are acceptable under LeetCode constraints and solve the problem efficiently.