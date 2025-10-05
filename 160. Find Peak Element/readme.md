# Find Peak Element - LeetCode

## Problem Explanation

The **Find Peak Element** problem asks us to find an index of a *peak* element in an array. A **peak element** is one that is strictly greater than its neighbors.

Formally:

* Given an integer array `nums`, return the index of any one of its peaks.
* The virtual elements `nums[-1]` and `nums[n]` are considered to be `-∞`, meaning the first and last elements can also be peaks.

### Example

```python
Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element, and its index is 2.

Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
Explanation: 6 is a peak element, and its index is 5.
```

### Constraints

* 1 <= nums.length <= 1000
* -2³¹ <= nums[i] <= 2³¹ - 1
* nums[i] != nums[i + 1] for all valid `i`.
* You must write an algorithm that runs in **O(log n)** time.

---

## Brute Force Solution

This is the simplest way to solve the problem by linearly scanning the array.

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Iterate through the array until the second-last element
        for i in range(len(nums) - 1):
            # If current element is greater than the next one, it's a peak
            if nums[i] > nums[i + 1]:
                return i
        
        # If no peak found in the loop, the last element must be the peak
        return len(nums) - 1
```

### Explanation of the Logic

1. Loop through the array and check if any element is greater than its next element.
2. If such an element is found, return its index — it’s a peak.
3. If no such element is found, then the last element is the peak (since `nums[n] = -∞`).

### Time and Space Complexity

* **Time Complexity:** `O(n)` — because we might need to check each element once.
* **Space Complexity:** `O(1)` — we only use a constant amount of memory.

### Drawback

Although simple, this approach doesn’t satisfy the problem’s requirement of `O(log n)` time. That’s where **Binary Search** helps.

---

## Binary Search Solution

We can use the concept of binary search to find the peak element efficiently.

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2  # Calculate middle index safely

            # If middle element is smaller than its left neighbor, move left
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1

            # If middle element is smaller than its right neighbor, move right
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1

            # Otherwise, we found a peak
            else:
                return m
```

### Explanation of the Logic

1. Use **binary search** to repeatedly divide the array in half.
2. Check the middle element `nums[m]` and its neighbors:

   * If the left neighbor is greater, the peak lies on the **left** side.
   * If the right neighbor is greater, the peak lies on the **right** side.
   * Otherwise, `nums[m]` is the peak.
3. Continue until you find the peak index.

This works because there’s always at least one peak in any array — the slope must eventually go down after going up.

### Time and Space Complexity

* **Time Complexity:** `O(log n)` — the search space is halved each time.
* **Space Complexity:** `O(1)` — we use only a few variables.

---

## Comparison Between Approaches

| Approach      | Time Complexity | Space Complexity | Meets O(log n)? | Description                                                       |
| ------------- | --------------- | ---------------- | --------------- | ----------------------------------------------------------------- |
| Brute Force   | O(n)            | O(1)             | No              | Simple scan to find where the sequence decreases.                 |
| Binary Search | O(log n)        | O(1)             | Yes             | Efficiently narrows down the search for a peak using slope logic. |

---

## Conclusion

The **Binary Search** solution is the most optimal because it reduces the search range by half each time, meeting the `O(log n)` requirement. The brute force solution is easier to understand but not suitable for large arrays where performance matters.