# Sort Colors - LeetCode

## Problem Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **red (0), white (1), and blue (2)**.

You must solve this problem **without using the library's sort function**.

### Example 1:

* Input: `nums = [2,0,2,1,1,0]`
* Output: `[0,0,1,1,2,2]`

### Example 2:

* Input: `nums = [2,0,1]`
* Output: `[0,1,2]`

### Constraints:

* `1 <= nums.length <= 300`
* `nums[i]` is either `0`, `1`, or `2`

### Follow-up:

Could you come up with a one-pass algorithm using only constant extra space?

---

## What is "Sort Colors"?

This problem is commonly known as the **Dutch National Flag problem**, where you are asked to sort an array that contains only three types of elements (0s, 1s, and 2s).

The challenge is to perform this in-place (without using extra space) and preferably in a single pass.

---

## Provided Solutions

### 1. Counting Sort Solution

```python
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3  # Initialize count array for 0s, 1s, and 2s
        
        # Count occurrences of each number
        for num in nums:
            count[num] += 1

        # Overwrite nums with the correct number of 0s, then 1s, then 2s
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
```

### Explanation:

* First loop counts the frequency of 0s, 1s, and 2s.
* Second loop overwrites the original array with the correct number of 0s, 1s, and 2s in that order.

### Time and Space Complexity:

* **Time:** O(n)
* **Space:** O(1) (only constant space used for `count`)

This is a simple and intuitive solution, but it uses **two passes**.

---

### 2. Three Pointers Solution (Dutch National Flag Algorithm)

```python
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1  # l tracks the end of 0s, r tracks the beginning of 2s
        i = 0  # i is the current index

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1  # Decrement i to re-check swapped element
            i += 1
```

### Explanation:

* Three pointers `l`, `r`, and `i` are used to track regions of 0s, 2s, and the current element.
* When `nums[i] == 0`, we move it to the left side.
* When `nums[i] == 2`, we move it to the right side.
* When `nums[i] == 1`, we just move on.

### Time and Space Complexity:

* **Time:** O(n) (only one pass over the array)
* **Space:** O(1) (only constant space used)

This is the **most optimal** solution as it does the work in one pass with constant space.

---

## Comparison of Solutions

| Solution       | Time Complexity | Space Complexity | Passes | Notes                            |
| -------------- | --------------- | ---------------- | ------ | -------------------------------- |
| Counting Sort  | O(n)            | O(1)             | 2      | Easy to understand and implement |
| Three Pointers | O(n)            | O(1)             | 1      | Most optimal and efficient       |

---

## Conclusion

The **Three Pointers (Dutch National Flag)** algorithm is the best approach for solving this problem. It ensures linear time complexity and constant space usage while sorting the array in a single traversal. This is especially useful when dealing with large datasets or performance-critical applications.
