# Valid Perfect Square - LeetCode

## Problem Explanation

The problem **Valid Perfect Square** asks us to determine whether a given positive integer `num` is a perfect square. A perfect square is defined as an integer that is the product of an integer multiplied by itself, for example:

* 16 is a perfect square because 4 × 4 = 16.
* 14 is not a perfect square because no integer squared equals 14.

The constraint is that we cannot use built-in library functions like `sqrt` to directly check if the number is a perfect square.

---

## Code Explanation

### Brute Force Solution

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            sq = i * i
            # If square exceeds num, no need to check further
            if sq > num:
                return False
            # If a match is found, num is a perfect square
            if sq == num:
                return True
```

* We iterate through numbers starting from 1.
* For each number `i`, we compute `i * i`.
* If `i * i` equals `num`, then `num` is a perfect square.
* If `i * i` becomes greater than `num`, we stop and return `False`.

This approach works but can be slow for very large values of `num`.

---

### Binary Search Solution

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            m = l + (r - l) // 2  # Find the middle number
            sq = m * m

            if sq > num:
                r = m - 1  # Search the left half
            elif sq < num:
                l = m + 1  # Search the right half
            else:
                return True  # Found an integer whose square equals num

        return False
```

* Instead of checking every number, we use binary search between `1` and `num`.
* At each step, compute the square of the middle value `m`.
* If `m * m` equals `num`, then `num` is a perfect square.
* If `m * m` is greater than `num`, search in the left half.
* If `m * m` is less than `num`, search in the right half.

This approach is much more efficient.

---

## Approach and Logic

### Brute Force:

* Check all numbers one by one up to `num`.
* Stop when the square exceeds `num`.
* Simple to understand but inefficient for large inputs.

### Binary Search:

* Use the fact that the squares of integers are sorted in increasing order.
* Perform binary search to quickly narrow down the possible candidate.
* Much faster than brute force for large values of `num`.

---

## Complexity Analysis

### Brute Force:

* **Time Complexity:** O(√n), because the loop runs until `i * i > num`. The maximum `i` needed is roughly √n.
* **Space Complexity:** O(1), since only a few variables are used.

### Binary Search:

* **Time Complexity:** O(log n), because the search space is halved in each iteration.
* **Space Complexity:** O(1), since only a few variables are used.

---

## Most Optimal Solution

The **binary search solution** is the most optimal:

* It works in O(log n) time, which is significantly faster than O(√n) for very large inputs.
* It uses constant space.
* This makes it the best approach for checking if a number is a perfect square without using built-in functions.

---


## Test Cases

```python
# Test Cases:
sol = Solution()

# Test Case 1:
num = 16
print(sol.isPerfectSquare(num))  # Expected Output: True

# Test Case 2:
num = 14
print(sol.isPerfectSquare(num))  # Expected Output: False
```