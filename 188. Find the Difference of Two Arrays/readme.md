# Find the Difference of Two Arrays - LeetCode

## Problem Explanation

The **Find the Difference of Two Arrays** problem requires identifying elements that exist in one array but not in the other. You are given two integer arrays, `nums1` and `nums2`, and you must return a list of two lists:

1. The first list contains all **distinct elements** from `nums1` that are **not present in `nums2`**.
2. The second list contains all **distinct elements** from `nums2` that are **not present in `nums1`**.

The order of elements in the result does not matter.

### Example

**Input:**

```python
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
```

**Output:**

```python
[[1, 3], [4, 6]]
```

Explanation: 1 and 3 exist only in `nums1`, while 4 and 6 exist only in `nums2`.

---

## Code Implementation with Comments

```python
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert both lists to sets to remove duplicates and allow O(1) lookups
        num1Set, num2Set = set(nums1), set(nums2)

        # Initialize two result lists to store unique elements
        res1, res2 = [], []

        # Find elements that are in num1Set but not in num2Set
        for num in num1Set:
            if num not in num2Set:
                res1.append(num)

        # Find elements that are in num2Set but not in num1Set
        for num in num2Set:
            if num not in num1Set:
                res2.append(num)

        # Return both lists as a combined result
        return [res1, res2]
```

---

## Approach and Logic

### 1. **Use of Sets**

The first step is to convert both arrays into sets. This removes duplicates and makes it easier to check membership efficiently.

### 2. **Finding Unique Elements**

We iterate over each set and check whether an element exists in the other set:

* If an element from `num1Set` is **not in `num2Set`**, it belongs to the first list.
* If an element from `num2Set` is **not in `num1Set`**, it belongs to the second list.

### 3. **Why Sets?**

Using sets instead of lists significantly reduces time complexity because membership checks (`in`) take O(1) on average for sets, whereas they take O(n) for lists.

### 4. **Alternative (Less Optimal) Approach**

A less optimal approach would be using nested loops to compare every element in `nums1` to every element in `nums2`, which would result in **O(n × m)** time complexity. By using sets, we improve this to **O(n + m)**.

---

## Example Dry Run

**Example Input:**

```python
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
```

**Step 1:** Convert to sets:

```
num1Set = {1, 2, 3}
num2Set = {1, 2}
```

**Step 2:**

* For `num1Set`: 1 and 2 exist in `num2Set`, but 3 does not → add 3 to `res1`.
* For `num2Set`: all elements (1, 2) exist in `num1Set` → `res2` remains empty.

**Output:**

```
[[3], []]
```

---

## Time and Space Complexity

* **Time Complexity:** `O(n + m)`

  * Creating sets from both arrays takes `O(n + m)`.
  * Iterating through both sets also takes `O(n + m)`.
  * Overall, the time complexity remains linear.

* **Space Complexity:** `O(n + m)`

  * We store both arrays as sets, and additional space is used for the output lists.

---

## Why This Solution is Optimal

This **Hash Set approach** is the most optimal because:

* It ensures that every lookup and comparison takes constant time.
* It eliminates duplicates automatically, reducing unnecessary work.
* It handles the problem efficiently even for large input sizes (up to 1000 elements as per constraints).

Thus, this approach provides the best trade-off between simplicity, efficiency, and clarity.

## Test Cases

``` python
# Test Case 1:
nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[1,3],[4,6]]

# Test Case 2:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[3],[]]

# Test Case 3:
nums1 = [4,5,6]
nums2 = [1,2,3]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[4,5,6],[1,2,3]]
```