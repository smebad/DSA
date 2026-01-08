# Count Number of Nice Subarrays - LeetCode

## Problem Description

The problem "Count Number of Nice Subarrays" asks you to determine the number of continuous subarrays in a given integer array `nums` that contain exactly `k` odd numbers. A subarray is considered "nice" if it has exactly `k` odd numbers.

### Examples

**Example 1:**

```
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The subarrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
```

**Example 2:**

```
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
```

**Example 3:**

```
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

### Constraints

* `1 <= nums.length <= 50000`
* `1 <= nums[i] <= 10^5`
* `1 <= k <= nums.length`

## Solution Approach: Three Pointers

This solution uses a three-pointer technique to efficiently count nice subarrays. The pointers help track the leftmost boundary (`l`), a secondary boundary for zeros before the first odd (`m`), and the right boundary (`r`) as we traverse the array.

### Python Code with Comments

```python
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd = 0, 0  # res stores the number of nice subarrays, odd stores count of odd numbers
        l, m = 0, 0      # l is the left pointer, m tracks the first odd after l when odd == k

        for r in range(len(nums)):  # r is the right pointer moving through the array
            if nums[r] % 2:         # Check if current element is odd
                odd += 1

            # If odd numbers exceed k, move left pointer to reduce count
            while odd > k:
                if nums[l] % 2:    # If nums[l] is odd, reduce odd count
                    odd -= 1
                l += 1             # Move left pointer forward
                m = l              # Reset m to start scanning for first odd number

            # If odd numbers equal k, count the valid subarrays
            if odd == k:
                while not nums[m] % 2:  # Skip even numbers at the start of the window
                    m += 1
                res += (m - l) + 1      # Add the number of valid subarrays ending at r

        return res
```

### Approach Explanation

1. Traverse the array using the right pointer `r`.
2. Keep track of the number of odd numbers encountered.
3. If the number of odd numbers exceeds `k`, increment the left pointer `l` until there are exactly `k` odd numbers.
4. When the number of odd numbers equals `k`, use pointer `m` to count the number of even numbers before the first odd in the window to calculate the total number of valid subarrays ending at `r`.
5. Sum all counts to get the total number of nice subarrays.

### Logic in Simple Words

* Use `r` to expand the window.
* Adjust `l` when too many odd numbers are in the window.
* Use `m` to count subarrays starting with any number of leading even numbers before the first odd.
* Add the number of possible subarrays for each position of `r` when the odd count is exactly `k`.

### Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the array once with the right pointer `r`. The left pointer `l` and secondary pointer `m` also move through the array but never exceed `n` steps cumulatively.
* **Space Complexity:** `O(1)`

  * Only a constant amount of extra space is used (`res`, `odd`, `l`, `m`).

### Why This is Optimal

* Only one traversal of the array is required.
* No nested loops over the array elements are used.
* The three-pointer method efficiently calculates the number of subarrays without checking every possible subarray explicitly.

### Test Cases

```python
# Test Case 1
nums = [1, 1, 2, 1, 1]
k = 3
print(Solution().numberOfSubarrays(nums, k))  # Expected Output: 2

# Test Case 2
nums = [2, 4, 6]
k = 1
print(Solution().numberOfSubarrays(nums, k))  # Expected Output: 0

# Test Case 3
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(Solution().numberOfSubarrays(nums, k))  # Expected Output: 16
```
