# Find All Numbers Disappeared in an Array - LeetCode

## Problem Explanation

You are given an array `nums` of length `n` where each element is between `1` and `n`. Some numbers may appear twice, while others may not appear at all. The task is to return a list of all numbers in the range `[1, n]` that do not appear in `nums`.

### Example 1

**Input:** `nums = [4,3,2,7,8,2,3,1]`
**Output:** `[5,6]`

### Example 2

**Input:** `nums = [1,1]`
**Output:** `[2]`

**Constraints:**

* `n == nums.length`
* `1 <= n <= 10^5`
* `1 <= nums[i] <= n`

**Follow-up:** Can you solve this without extra space and in O(n) runtime?

---

## Solutions and Explanations

We will go through four different approaches: Hash-Set, Boolean Array, Sorting, and Negative Marking. Each approach has trade-offs in terms of time and space.

---

### 1. Hash-Set Solution

```python
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        store = set(range(1, n + 1))  # Create a set with all numbers from 1 to n

        for num in nums:
            store.discard(num)  # Remove numbers that appear in nums

        return list(store)  # Remaining numbers are missing
```

**Explanation:**

* We start with a set containing all numbers from `1` to `n`.
* As we iterate through `nums`, we remove each number from the set.
* At the end, the set contains only the missing numbers.

**Complexity:**

* Time: `O(n)` (iterating through `nums` and set operations are average `O(1)`)
* Space: `O(n)` (we store up to `n` numbers in the set)

---

### 2. Boolean Array Solution

```python
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mark = [False] * n  # Boolean array to mark presence

        for num in nums:
            mark[num - 1] = True  # Mark the index corresponding to the number

        res = []
        for i in range(1, n + 1):
            if not mark[i - 1]:  # If not marked, the number is missing
                res.append(i)
        return res
```

**Explanation:**

* We create a boolean array of size `n` initialized with `False`.
* For every number in `nums`, mark its corresponding index.
* The unmarked indices correspond to missing numbers.

**Complexity:**

* Time: `O(n)`
* Space: `O(n)` (extra boolean array)

---

### 3. Sorting Solution

```python
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()  # Sort the list

        res = []
        idx = 0
        for num in range(1, n + 1):
            while idx < n and nums[idx] < num:
                idx += 1  # Move pointer until nums[idx] >= num
            if idx == n or nums[idx] > num:
                res.append(num)  # If number not found, it's missing
        return res
```

**Explanation:**

* First, we sort the input array.
* Then we check for each number from `1` to `n` whether it exists in `nums`.
* If not found, add it to the result.

**Complexity:**

* Time: `O(n log n)` due to sorting
* Space: `O(1)` (ignoring the input array)

---

### 4. Negative Marking Solution (Optimal)

```python
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1  # Convert number to index
            nums[i] = -1 * abs(nums[i])  # Mark index as negative

        res = []
        for i, num in enumerate(nums):
            if num > 0:  # Positive means index + 1 is missing
                res.append(i + 1)
        return res
```

**Explanation:**

* For each number, mark the index it corresponds to as negative.
* At the end, any index that remains positive means its number was missing.

**Complexity:**

* Time: `O(n)`
* Space: `O(1)` (in-place, does not use extra data structures)

This is the most optimal solution because it achieves both `O(n)` time and `O(1)` extra space.

---

## Comparing the Approaches

| Approach         | Time Complexity | Space Complexity | Notes                                         |
| ---------------- | --------------- | ---------------- | --------------------------------------------- |
| Hash-Set         | O(n)            | O(n)             | Easy, but uses extra memory                   |
| Boolean Array    | O(n)            | O(n)             | Similar to Hash-Set, but uses a boolean array |
| Sorting          | O(n log n)      | O(1)             | Slower due to sorting                         |
| Negative Marking | O(n)            | O(1)             | Most optimal, modifies input in place         |

**Final Recommendation:** Use the **Negative Marking Solution** for large inputs, as it is both time and space efficient.