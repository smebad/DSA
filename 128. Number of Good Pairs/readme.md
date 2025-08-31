# Number of Good Pairs - LeetCode

## Problem Statement

Given an array of integers `nums`, return the number of **good pairs**.

A pair `(i, j)` is called good if:

* `nums[i] == nums[j]`
* `i < j`

### Example 1:

**Input:** nums = \[1,2,3,1,1,3]
**Output:** 4
**Explanation:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5).

### Example 2:

**Input:** nums = \[1,1,1,1]
**Output:** 6
**Explanation:** Every pair in the array is good.

### Example 3:

**Input:** nums = \[1,2,3]
**Output:** 0

### Constraints

* 1 <= nums.length <= 100
* 1 <= nums\[i] <= 100

---

## Solutions

We explore three approaches: **Brute Force**, **Mathematical Counting**, and **Hash Map Counting**.

---

### 1. Brute Force Solution

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        # Compare every pair (i, j)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1  # Increase count if pair is good
        return res
```

#### Explanation:

* We loop through each element and check it against every element that comes after it.
* If they are equal, we count it as a good pair.

#### Complexity:

* **Time Complexity:** O(n²) because we check every possible pair.
* **Space Complexity:** O(1) since we only use a counter.

This solution works but is inefficient for large arrays.

---

### 2. Mathematical Counting Solution

```python
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)  # Count frequency of each number
        res = 0
        for num, c in count.items():
            # For each number, number of good pairs = c choose 2 = c * (c - 1) // 2
            res += c * (c - 1) // 2
        return res
```

#### Explanation:

* Count how many times each number appears.
* If a number appears `c` times, then the number of ways to form good pairs is:

  **c choose 2 = c \* (c - 1) / 2**

Example: If `1` appears 4 times → pairs = 4 \* 3 / 2 = 6.

#### Complexity:

* **Time Complexity:** O(n) for counting frequencies.
* **Space Complexity:** O(n) for storing counts.

This is much faster than brute force.

---

### 3. Hash Map Counting Solution

```python
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        for num in nums:
            res += count[num]  # Add how many times we've seen this number before
            count[num] += 1   # Update frequency
        return res
```

#### Explanation:

* Instead of counting first and then calculating, we build pairs as we traverse the array.
* For each number:

  * The number of pairs it can form is equal to how many times we’ve already seen it.
  * We add that count to the result, then update the count.

Example: For `[1,2,3,1,1,3]`:

* First `1`: seen before = 0 → add 0.
* Second `1`: seen before = 1 → add 1.
* Third `1`: seen before = 2 → add 2.
* And so on...

#### Complexity:

* **Time Complexity:** O(n) because we traverse once.
* **Space Complexity:** O(n) for the hash map.

This method is both efficient and simple.

---

## Comparison of Solutions

1. **Brute Force:** Easy to understand but very slow (O(n²)).
2. **Mathematical Counting:** Uses frequency counts and combinatorics (O(n)), but requires two steps: counting and computing.
3. **Hash Map Counting:** Single pass (O(n)) and directly counts pairs while traversing.

---

## Optimal Solution

The **Hash Map Counting** solution is the most optimal:

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)
* Efficient because it avoids nested loops and directly builds the result while traversing.

It is preferred over brute force for large inputs and is more intuitive in implementation compared to the math solution.
