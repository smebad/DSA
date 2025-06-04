# Remove Element - LeetCode

## Problem Description

The **Remove Element** problem is a classic array manipulation challenge commonly found on platforms like LeetCode.

**Problem Statement:**

> Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of the elements may be changed. Return the number of elements in `nums` that are not equal to `val`.

You need to ensure that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements beyond `k` are not important.

---

## Example

**Input:**

```
nums = [3,2,2,3], val = 3
```

**Output:**

```
2, nums = [2,2,_,_]
```

**Input:**

```
nums = [0,1,2,2,3,0,4,2], val = 2
```

**Output:**

```
5, nums = [0,1,4,0,3,_,_,_]
```

---

## Two Solutions

### 1. Two-Pointer (Optimal) Approach

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Counter for non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to the front
                k += 1  # Increase the valid count
        return k
```

#### Explanation:

* `k` keeps track of the next position to place a non-val element.
* Iterate through each element using `i`.
* If the element is not equal to `val`, place it at position `k`, and increment `k`.
* Return `k` as the count of elements not equal to `val`.

### 2. Brute Force Approach

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []  # Temporary list to hold non-val elements
        for num in nums:
            if num != val:
                tmp.append(num)  # Add non-val element to tmp
        for i in range(len(tmp)):
            nums[i] = tmp[i]  # Overwrite original list
        return len(tmp)
```

#### Explanation:

* Store all non-val elements in a temporary list.
* Copy them back to the original `nums` array.
* Return the count of non-val elements.

---

## Comparison and Key Concepts

| Approach    | Time Complexity | Space Complexity | In-Place | Explanation                                                  |
| ----------- | --------------- | ---------------- | -------- | ------------------------------------------------------------ |
| Two-Pointer | O(n)            | O(1)             | Yes      | Most optimal. Uses two pointers to filter elements in place. |
| Brute Force | O(n)            | O(n)             | No       | Easy to understand, but creates an extra list.               |

---

## Why Two-Pointer is Optimal

* The two-pointer method does not use extra memory.
* It directly modifies the input array in-place.
* It is faster in terms of real-world performance due to less memory allocation.
* Works well even for large arrays.

---

## Test Cases

```python
# Test Case 1:
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))  # Output: 2

# Test Case 2:
nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums, val))  # Output: 5
```

---

## Constraints

* 0 <= nums.length <= 100
* 0 <= nums\[i] <= 50
* 0 <= val <= 100
