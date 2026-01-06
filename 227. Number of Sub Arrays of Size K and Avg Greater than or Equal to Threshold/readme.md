# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold - LeetCode

## Problem Description

"Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold" is a problem where we are given an array of integers `arr` and two integers `k` and `threshold`. The task is to find the number of contiguous sub-arrays of size `k` whose average value is greater than or equal to `threshold`.

In other words, for each sub-array of length `k`, we compute its average and count it if the average meets or exceeds the threshold.

### Example 1:

```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively.
```

### Example 2:

```
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5.
```

### Constraints:

* 1 <= arr.length <= 10^5
* 1 <= arr[i] <= 10^4
* 1 <= k <= arr.length
* 0 <= threshold <= 10^4

---

## Solution Explanation

The problem can be efficiently solved using the **Sliding Window** technique.

### Sliding Window Approach:

1. Initialize a running sum `curSum` with the sum of the first `k-1` elements.
2. Slide a window of size `k` through the array:

   * Add the next element in the window to `curSum`.
   * Check if the average (`curSum / k`) meets or exceeds the threshold.
   * Increment the result counter if it does.
   * Subtract the first element of the window to slide the window forward.
3. Continue this process until the window reaches the end of the array.

This avoids recalculating the sum for each sub-array from scratch, which would be inefficient for large arrays.

### Code with Comments:

```python
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        # Initialize current sum with the sum of the first k-1 elements
        curSum = sum(arr[:k - 1])

        # Slide the window over the array
        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]  # Include the new element in the window
            if (curSum / k) >= threshold:  # Check if the average meets the threshold
                res += 1  # Count this sub-array
            curSum -= arr[L]  # Remove the leftmost element as window slides forward
        return res
```

### Approach & Logic:

* Use a sliding window of length `k`.
* Maintain a running sum for efficiency.
* Compare the average to the threshold instead of recalculating the sum each time.
* Increment a counter when the condition is satisfied.

### Time Complexity:

* **O(n)**, where `n` is the length of the array `arr`. The array is traversed once.

### Space Complexity:

* **O(1)**, since only a few variables are used regardless of the input size.

This is the most optimal approach because it avoids nested loops and recalculations.

---

## Test Cases:

```python
# Test Case 1
arr1 = [2, 2, 2, 2, 5, 5, 5, 8]
k1 = 3
threshold1 = 4
print(Solution().numOfSubarrays(arr1, k1, threshold1))  # Expected output: 3

# Test Case 2
arr2 = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k2 = 3
threshold2 = 5
print(Solution().numOfSubarrays(arr2, k2, threshold2))  # Expected output: 6
```