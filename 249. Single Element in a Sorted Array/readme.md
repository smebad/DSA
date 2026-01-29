# Single Element in a Sorted Array - LeetCode

## 1. Problem Explanation

The problem **Single Element in a Sorted Array** gives us a sorted array of integers where:

* Every element appears **exactly twice**.
* Except for **one element**, which appears **only once**.

Our task is to find and return that single element.

### Important Constraints

* The array is already **sorted**.
* We must solve the problem in:

  * **O(log n)** time
  * **O(1)** extra space

This means we are expected to use **binary search**, not a linear scan or hash map.

### Example

Input:

```
[1,1,2,3,3,4,4,8,8]
```

Output:

```
2
```

Here, all numbers appear twice except `2`, so the answer is `2`.

---

## 2. Code With Detailed Comments
```python
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  # Binary search boundaries

        while l <= r:
            # Middle index
            m = l + ((r - l) // 2)

            # Check if nums[m] is the single element
            # It must be different from both neighbors
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and
                (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]

            # Determine size of left side
            # If nums[m] == nums[m-1], then the pair starts at m-1
            # Otherwise, pair starts at m
            leftSize = m - 1 if nums[m - 1] == nums[m] else m

            # If left side length is odd, the single element is on the left
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1
```

---

## 3. Solution Approach and Logic

### Key Observation

In a perfectly paired array:

* Before the single element, pairs start at **even indices**.
* After the single element, pairs start at **odd indices**.

This pattern breaks exactly at the single element.

### Intuition

We use binary search to check:

* Is the middle element the single one?
* If not, which side is broken (odd length)?

We then discard half the array just like normal binary search.

---

## 4. Step-by-Step Example

Input:

```
[1,1,2,3,3,4,4,8,8]
```

Indices:

```
 0 1 2 3 4 5 6 7 8
```

* Middle index = 4 → value = 3
* It forms a pair with index 3
* Left side size = 3 (odd)
* So the single element is on the **left side**

Binary search continues until `2` is found.

---

## 5. Why Binary Search Works Here

Because:

* The array is sorted
* All elements are paired except one
* Pair positions follow a strict even/odd pattern

This structure allows us to eliminate half the search space each time.

---

## 6. Time and Space Complexity

### Binary Search Solution

* **Time Complexity:** O(log n)

  * We cut the array in half each iteration.

* **Space Complexity:** O(1)

  * Only a few variables are used.

---

## 7. Why This Is the Most Optimal Solution

This solution is optimal because:

* It satisfies the strict requirement of **O(log n)** time.
* It uses **constant memory**.
* It leverages the **sorted structure and pairing pattern**.


No solution can do better than O(log n) for this problem because we must at least inspect values using binary search logic.
