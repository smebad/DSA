# Convert an Array Into a 2D Array With Conditions - LeetCode

## 1. Problem Explanation

The problem **"Convert an Array Into a 2D Array With Conditions"** asks us to take a given array `nums` and convert it into a 2D array (a list of rows) under three important conditions:

1. The 2D array must contain **all elements of the original array**.
2. **Each row must contain distinct integers**, meaning no duplicates inside the same row.
3. The number of rows must be **as small as possible**.

If multiple valid answers exist, any one is acceptable.

### Key Idea

If a number appears many times, say `k` times, then we need **at least `k` rows**, because each row can contain that number at most once.

For example, if the number `1` appears **3 times**, we need at least 3 rows to place each `1` in its own row.

---

## 2. Code with Detailed Comments

```python
from collections import defaultdict
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Dictionary to count how many times each number has appeared so far
        count = defaultdict(int)

        # Final 2D array result
        res = []

        for num in nums:
            # The row this number should go to is determined by how many times
            # it has appeared already. For example, the 3rd occurrence of a number
            # must go to row index 2.
            row = count[num]

            # If this row does not exist yet, create a new row
            if len(res) == row:
                res.append([])

            # Place the number in the appropriate row
            res[row].append(num)

            # Increase the count for this number
            count[num] += 1

        return res
```

---

## 3. Explanation of the Solution and Logic

### How the Approach Works

The main observation is:

* If a number appears multiple times, we must spread those occurrences across multiple rows.

So instead of manually building rows while checking duplicates, the above solution uses a simple rule:

* The **first occurrence** of a number goes to **row 0**.
* The **second occurrence** goes to **row 1**.
* The **third occurrence** goes to **row 2**, and so on.

### Why This Works

Because:

* Each row now contains only **one copy** of each number.
* Rows are created **only when needed**, making the number of rows minimal.

### Simple Example

For input:

```
nums = [1,3,4,1,2,3,1]
```

How many times each number has appeared so far:

* First `1` → row 0
* First `3` → row 0
* First `4` → row 0
* Second `1` → row 1
* First `2` → row 0
* Second `3` → row 1
* Third `1` → row 2

Final result:

```
[
  [1, 3, 4, 2],
  [1, 3],
  [1]
]
```

### Why This Strategy Is Optimal

* We only create a new row when we are forced to (when an element appears again).
* No unnecessary rows are created.

This ensures the minimum possible number of rows.

### Difference From Other Approaches

A beginner might try to:

* Build rows one at a time,
* Check if an element already exists in the row,
* If yes, try another row.

That approach is:

* More complicated,
* Harder to code,
* More prone to mistakes.

The provided approach is elegant because it uses counts instead of searching.

---

## 4. Time and Space Complexity

### Time Complexity: **O(n)**

* We loop through the array exactly once.
* Every operation inside the loop is constant time.

This is optimal because we must look at every element at least once.

### Space Complexity: **O(n)**

* The 2D result array stores all elements once.
* The `count` dictionary stores at most one entry per unique number.

This is also optimal because the output itself requires O(n) space.

### Why This Solution Is Optimal

You cannot do better than:

* **O(n)** time (must read all elements)
* **O(n)** space (must store the 2D array)

The method used ensures the minimum number of rows and avoids unnecessary checks.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
nums1 = [1,3,4,1,2,3,1]
print(sol.findMatrix(nums1))  # Expected: [[1,3,4,2], [1,3], [1]]

# Test Case 2
nums2 = [1,2,3,4]
print(sol.findMatrix(nums2))  # Expected: [[4,3,2,1]]
```