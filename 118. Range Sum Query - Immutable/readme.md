# Range Sum Query Immutable - LeetCode

## 1. Problem Explanation

The **Range Sum Query - Immutable** problem asks us to efficiently calculate the sum of elements in a given range of an integer array multiple times.

You are given:

* An integer array `nums`.
* Multiple queries of the form `(left, right)`.
* Each query asks: **"What is the sum of all numbers from index `left` to index `right` inclusive?"**

The challenge is to make these queries efficient, especially when the number of queries can be very large.

**Example:**

```
nums = [-2, 0, 3, -5, 2, -1]
Query 1: sumRange(0, 2) => (-2) + 0 + 3 = 1
Query 2: sumRange(2, 5) => 3 + (-5) + 2 + (-1) = -1
Query 3: sumRange(0, 5) => (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

Constraints:

* 1 <= nums.length <= 10^4
* -10^5 <= nums\[i] <= 10^5
* At most 10^4 queries.

---

## 2. Code with Comments

### Prefix Sum Approach (Optimized)

```python
class NumArray:
    def __init__(self, nums):
        # Store prefix sums
        self.prefix = []
        cur = 0
        for num in nums:
            cur += num  # cumulative sum
            self.prefix.append(cur)

    def sumRange(self, left, right):
        # Total sum from start to 'right'
        rightSum = self.prefix[right]
        # Total sum from start to 'left - 1', if left > 0
        leftSum = self.prefix[left - 1] if left > 0 else 0
        # Range sum = right sum - left sum
        return rightSum - leftSum
```

### Brute Force Approach (Less Efficient)

```python
class NumArray:
    def __init__(self, nums):
        self.nums = nums  # store original array

    def sumRange(self, left, right):
        res = 0
        for i in range(left, right + 1):
            res += self.nums[i]  # add each element in the range
        return res
```

---

## 3. Approach and Logic

### Brute Force Solution

* **Idea:** For each query, loop through the elements from `left` to `right` and add them up.
* **Steps:**

  1. Start with `res = 0`.
  2. Iterate over the range `left` to `right`.
  3. Add each element to `res`.
  4. Return `res`.
* **Drawback:** For each query, we may have to loop through many elements, making it slow when there are many queries.

### Prefix Sum Solution (Optimal)

* **Idea:** Precompute cumulative sums so that each range sum can be calculated in constant time.
* **Steps:**

  1. Build a `prefix` array where `prefix[i]` stores the sum of elements from `nums[0]` to `nums[i]`.
  2. For a query `(left, right)`, the range sum is:

     * `prefix[right] - prefix[left - 1]` if `left > 0`.
     * `prefix[right]` if `left == 0`.
* **Advantage:** After the initial setup, each query takes **O(1)** time.

---

## 4. Complexity Analysis

| Approach    | Time per Query | Preprocessing Time | Space Complexity | When to Use                   |
| ----------- | -------------- | ------------------ | ---------------- | ----------------------------- |
| Brute Force | O(n)           | O(1)               | O(1)             | Small inputs or few queries   |
| Prefix Sum  | O(1)           | O(n)               | O(n)             | Large inputs and many queries |

### Why Prefix Sum is Optimal

* When the number of queries is large, the cost of O(n) per query in the brute force method becomes too high.
* Prefix sum reduces query time to O(1), meaning the query time stays constant no matter the range size.
* The small extra memory (O(n)) for storing prefix sums is a worthwhile trade-off for the huge speed improvement in query handling.

---

## 5. Final Recommendation

* **If you have only a few queries:** Brute force is fine.
* **If you have many queries:** Use the **Prefix Sum** method for efficiency.