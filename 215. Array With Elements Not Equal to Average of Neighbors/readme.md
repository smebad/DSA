# Array With Elements Not Equal to Average of Neighbors - LeetCode

## Problem Explanation

In this problem, you are given a 0-indexed array of **distinct integers**. Your task is to rearrange the array so that **no element is equal to the average of its immediate neighbors**.

Formally, for every index `i` such that `1 <= i < n - 1`:

(nums[i - 1] + nums[i + 1]) / 2 != nums[i]

You may return **any valid rearrangement** that satisfies this condition.

This problem tests your understanding of array manipulation, greedy strategies, and recognizing patterns that avoid symmetry.

---

## Key Observation

If the array is sorted and values are placed in a zig-zag (low, high, low, high) pattern, the middle element will never be exactly the average of its neighbors. This works because the neighbors are intentionally chosen to be far apart.

---

## Greedy Solution (With Comments)

```python
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Sort the array so we can control placement order
        nums.sort()

        # Result array to store rearranged elements
        res = []

        # Two pointers: one at the smallest element, one at the largest
        l, r = 0, len(nums) - 1

        # Continue until all elements are placed
        while len(res) != len(nums):
            # Place the smallest remaining element
            res.append(nums[l])
            l += 1

            # Place the largest remaining element (if any left)
            if l <= r:
                res.append(nums[r])
                r -= 1

        return res
```

These comments explain exactly what each step is doing so you can easily recall the logic later.

---

## Approach and Logic Explained Simply

### Step 1: Sort the Array

Sorting helps us clearly separate small and large values. This makes it easier to avoid placing numbers that could become the average of their neighbors.

### Step 2: Use Two Pointers

* `l` starts at the smallest number
* `r` starts at the largest number

### Step 3: Alternate Placement

We build the result array by:

1. Adding the smallest remaining number
2. Adding the largest remaining number

This creates a pattern like:

small, large, small, large, ...

### Why This Works

Because the neighbors of any middle element are intentionally far apart in value, their average will not match the middle element.

For example:

If neighbors are `2` and `10`, their average is `6`, which is unlikely to be exactly the middle number placed.

Since all numbers are distinct, equality is avoided.

---

## Alternative Perspective

Another common valid approach is to sort the array and then rearrange it by placing the first half at even indices and the second half at odd indices. Both strategies rely on **breaking symmetry** to avoid averages.

Your solution is simpler to implement and easier to reason about.

---

## Time and Space Complexity

### Time Complexity

* Sorting the array takes **O(n log n)**
* Building the result array takes **O(n)**

Overall time complexity: **O(n log n)**

### Space Complexity

* An additional array `res` is used

Space complexity: **O(n)**

---

## Most Optimal Solution

This greedy solution is optimal for this problem because:

* Sorting is necessary to control placement order
* The problem allows returning any valid arrangement
* The solution guarantees correctness without backtracking or extra checks

Given the constraints (up to 10^5 elements), this approach is efficient and safe.

---

## Test Cases:
```python
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    print("Test Case 1 Output:", solution.rearrangeArray(nums1))
    
    # Test Case 2
    nums2 = [6, 2, 0, 9, 7]
    print("Test Case 2 Output:", solution.rearrangeArray(nums2))
    
    # Additional Test Case 3
    nums3 = [10, 20, 30, 40, 50, 60]
    print("Test Case 3 Output:", solution.rearrangeArray(nums3))
    
    # Additional Test Case 4
    nums4 = [5, 3, 8, 6, 2, 7, 4, 1]
    print("Test Case 4 Output:", solution.rearrangeArray(nums4))
```