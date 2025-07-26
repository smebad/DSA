# Next Greater Element I - LeetCode

## Problem Statement

The **Next Greater Element I** problem asks us to find the next greater number for elements in one array (`nums1`) by looking at their position and relationship in a second array (`nums2`).

**Definition:** The next greater element for an element `x` in an array is the first greater element that appears to the **right** of `x` in the same array.

You're given:

* Two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each element in `nums1`, determine its **next greater element** in `nums2`. If it does not exist, return `-1`.

---

### Example 1:

```
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
Explanation:
- 4 has no greater element to its right in nums2
- 1's next greater element is 3
- 2 has no greater element to its right
```

### Example 2:

```
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
Explanation:
- 2's next greater element is 3
- 4 has no greater element to its right
```

---

## Constraints

* 1 <= nums1.length <= nums2.length <= 1000
* 0 <= nums1\[i], nums2\[i] <= 10^4
* All integers in nums1 and nums2 are unique
* All elements in nums1 appear in nums2

---

## Solution 1: Brute Force with Hash Map

```python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num: i for i, num in enumerate(nums1)}  # map each number in nums1 to its index
        res = [-1] * len(nums1)  # initialize result list with -1

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
```

### Explanation:

* We store the index of each number from `nums1` in a hash map for quick lookup.
* For each element in `nums2`, if it exists in `nums1`, we search to its right for the next greater element.
* If found, we update the corresponding index in `res` with the next greater element.

### Time Complexity:

* **O(m \* n)** where `m = len(nums1)` and `n = len(nums2)`
* For each element in `nums2`, we may loop again to find the next greater element.

### Space Complexity:

* **O(m)** for the hash map and result list.

---

## Solution 2: Optimized Stack-Based Approach

```python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num: i for i, num in enumerate(nums1)}  # map each number in nums1 to its index
        res = [-1] * len(nums1)

        stack = []  # monotonically decreasing stack
        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                if val in nums1Idx:
                    idx = nums1Idx[val]
                    res[idx] = num
            if num in nums1Idx:
                stack.append(num)
        return res
```

### Explanation:

* Traverse `nums2` once.
* Maintain a **monotonic decreasing stack**: elements that haven't found their next greater element yet.
* Whenever we find a number `num` greater than `stack[-1]`, it means `num` is the next greater element for that number.
* Pop from stack and update the result.

### Time Complexity:

* **O(m + n)** where `m = len(nums1)` and `n = len(nums2)`
* Each element is pushed and popped at most once.

### Space Complexity:

* **O(m)** for the result and hash map.

---

## Comparison of Both Approaches

| Approach                    | Time Complexity | Space Complexity | Explanation                                            |
| --------------------------- | --------------- | ---------------- | ------------------------------------------------------ |
| Brute Force + HashMap       | O(m \* n)       | O(m)             | Simple to understand, but inefficient for large inputs |
| Stack-based Monotonic Stack | O(m + n)        | O(m)             | Optimal and efficient for larger arrays                |

The **stack-based solution** is the most optimal because it avoids nested loops and processes each element in `nums2` only once, using the stack to track unresolved elements.