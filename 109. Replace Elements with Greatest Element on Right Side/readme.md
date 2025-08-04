# Replace Elements with Greatest Element on Right Side - LeetCode

## Problem Description

Given an integer array `arr`, the goal is to replace each element with the greatest element among the elements to its right. The last element is always replaced with `-1` since there are no elements to its right.

### Example 1

```
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> greatest to the right is 18
- index 1 --> greatest to the right is 6
- index 2 --> greatest to the right is 6
- index 3 --> greatest to the right is 6
- index 4 --> greatest to the right is 1
- index 5 --> no element to the right, so -1
```

### Example 2

```
Input: arr = [400]
Output: [-1]
Explanation: No element to the right.
```

### Constraints

* 1 <= arr.length <= 10^4
* 1 <= arr\[i] <= 10^5

---

## Code with Comments

```python
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n  # Initialize the answer array of the same length
        rightMax = -1  # Start with -1 as the rightmost element

        # Traverse the array in reverse
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax  # Set the current index to the greatest element on the right
            rightMax = max(arr[i], rightMax)  # Update the rightMax if current is greater

        return ans
```

---

## Explanation of the Solution

### Approach

This solution works by scanning the array from **right to left**:

1. It keeps track of the maximum value seen so far (`rightMax`).
2. For each element, it updates the result array with the current `rightMax`.
3. Then, it updates `rightMax` to be the maximum between the current element and `rightMax`.
4. This ensures that for any given index, you always know the largest element that appears after it.

### Why This Works

The suffix-max approach guarantees that we always know the maximum of all elements to the right of the current element. Since we go in reverse, we only need one pass.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)` where `n` is the length of the array. We only loop through the array once.
* **Space Complexity:** `O(1)` if we modify the array in place, but `O(n)` in the current implementation because we use an additional array `ans`.

---

## Optimality

This solution is **optimal** because:

* It solves the problem in a **single pass**.
* It does **not require nested loops** or extra data structures.
* It uses **constant auxiliary space** apart from the result array.

---

## Test Cases

```python
# Test Case 1:
arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))  # Output: [18,6,6,6,1,-1]

# Test Case 2:
arr = [400]
print(Solution().replaceElements(arr))  # Output: [-1]
```