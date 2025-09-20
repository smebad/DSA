# Relative Sort Array - LeetCode

## Problem Explanation

We are given two arrays **arr1** and **arr2**. All elements in **arr2** are distinct and appear in **arr1**. The task is to sort **arr1** such that:

1. The relative order of elements in **arr1** is the same as their order in **arr2**.
2. Elements not in **arr2** should be placed at the end of **arr1**, in ascending order.

### Example 1:

**Input:**

```
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
```

**Output:**

```
[2,2,2,1,4,3,3,9,6,7,19]
```

### Example 2:

**Input:**

```
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
```

**Output:**

```
[22,28,8,6,17,44]
```

---

## Brute Force Solution

```python
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        # For each number in arr2, collect its occurrences from arr1
        for num2 in arr2:
            for i, num1 in enumerate(arr1):
                if num1 == num2:
                    res.append(num1)
                    arr1[i] = -1  # Mark as used

        # Sort arr1 and append remaining numbers to result
        arr1.sort()
        for i in range(len(res), len(arr1)):
            res.append(arr1[i])

        return res
```

### Explanation:

1. Loop through each number in **arr2**.
2. For each number, check **arr1** and add matches to the result.
3. Mark used elements as -1.
4. Sort remaining numbers in **arr1** and append them.

**Time Complexity:** `O(m * n + n log n)`

* `m * n` for checking each pair of numbers.
* `n log n` for sorting remaining elements.

**Space Complexity:** `O(1)` (excluding the output array).

This works but is inefficient for larger arrays.

---

## Hashmap Solution (Optimized)

```python
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Count frequency of each number in arr1
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        res = []
        # Add elements in arr2 order
        for num in arr2:
            res += [num] * count.pop(num)

        # Add remaining numbers sorted
        for num in sorted(count):
            res += [num] * count[num]

        return res
```

### Explanation:

1. Count frequency of all numbers in **arr1**.
2. For each number in **arr2**, append it the number of times it appears.
3. Remove processed numbers from the count dictionary.
4. Append the remaining numbers in sorted order.

**Time Complexity:** `O(n + m + n log n)`

* `O(n)` to count frequencies.
* `O(m)` to build ordered result from **arr2**.
* `O(k log k)` to sort remaining numbers (k ≤ n).

**Space Complexity:** `O(n)` for the dictionary and output.

This is more efficient and **optimal** for this problem compared to brute force.

---

## Conclusion

* **Brute Force:** Straightforward but inefficient (`O(m * n + n log n)`).
* **Hashmap:** Efficient and optimal (`O(n log n)` in worst case).

The **Hashmap solution** is the recommended approach because it avoids redundant scanning of arrays and handles frequency counting effectively.

---

## Test Cases

```python
# Test Case 1:
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(sol.relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,9,6,7,19]

# Test Case 2:
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(sol.relativeSortArray(arr1, arr2))  # Output: [22,28,8,6,17,44]
```