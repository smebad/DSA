# Contiguous Array - LeetCode

## Problem Description

"Contiguous Array" is a problem where you are given a binary array `nums` (containing only 0s and 1s). The task is to find the **maximum length of a contiguous subarray** that contains an equal number of 0s and 1s.

In simpler words, you need to find the longest consecutive sequence in the array where the count of 0s equals the count of 1s.

### Examples

**Example 1:**

```
Input: nums = [0,1]
Output: 2
Explanation: The entire array has 1 zero and 1 one.
```

**Example 2:**

```
Input: nums = [0,1,0]
Output: 2
Explanation: Either [0,1] or [1,0] has equal number of 0s and 1s.
```

**Example 3:**

```
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal 0s and 1s.
```

### Constraints

* 1 <= nums.length <= 10^5
* nums[i] is either 0 or 1.

---

## Solution Explanation

We use a **hashmap** to solve this problem efficiently. The key idea is to treat 0 as -1 and 1 as 1. Then the problem becomes finding the **longest subarray with sum 0**.

### Step-by-Step Logic

1. Initialize two counters `zero` and `one` to keep track of the count of 0s and 1s.
2. Use a dictionary `diff_index` to store the **first occurrence of a difference** `(one - zero)`.
3. Iterate through the array:

   * Update `zero` or `one` based on the current element.
   * Calculate the difference `one - zero`.
   * If this difference was seen before, it means there is a subarray between the first occurrence and the current index with equal 0s and 1s.
   * Update the maximum length `res` accordingly.
   * If the difference is not in the dictionary, store it with the current index.

### Code with Comments

```python
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = one = res = 0  # counters for 0s, 1s and result
        diff_index = {}  # stores first occurrence of difference (one - zero)

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            # store the first occurrence of this difference
            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero  # if counts are equal from start
            else:
                idx = diff_index[one - zero]  # get first index with same diff
                res = max(res, i - idx)  # max length so far

        return res
```

### Approach in Simple Words

* Convert 0 to -1 to track running sum (optional in logic above, counts difference used).
* Keep track of first occurrences of each difference.
* If the same difference appears again, the subarray between the first and current index has equal 0s and 1s.
* Update the maximum length.

### Why This Works

The difference `one - zero` effectively represents the net number of 1s over 0s. If we see the same difference at two indices, the subarray in between balances out the counts.

### Complexity Analysis

* **Time Complexity:** O(n) — single pass through the array.
* **Space Complexity:** O(n) — hashmap to store differences. Worst case: all differences are unique.

### Test Cases

```python
sol = Solution()

# Test Case 1
nums1 = [0, 1]
print(sol.findMaxLength(nums1))  # Output: 2

# Test Case 2
nums2 = [0, 1, 0]
print(sol.findMaxLength(nums2))  # Output: 2

# Test Case 3
nums3 = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(sol.findMaxLength(nums3))  # Output: 6
```
