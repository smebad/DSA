# Successful Pairs of Spells and Potions - LeetCode

## 1. Problem Explanation

In this problem, you are given two arrays:

* `spells`: represents the strength of each spell.
* `potions`: represents the strength of each potion.

You are also given an integer `success`.

A pair `(spell, potion)` is considered **successful** if:

spell * potion >= success

Your task is to return an array `pairs` where:

pairs[i] = number of potions that can form a successful pair with spells[i]

In simple words:
For every spell, count how many potions are strong enough so that their product reaches at least `success`.

---

## 2. Code With Comments

```python
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Step 1: Sort potions so we can apply binary search
        potions.sort()
        
        res = []  # This will store the answer for each spell

        # Step 2: For each spell, find how many potions are successful
        for s in spells:
            l, r = 0, len(potions) - 1
            idx = len(potions)  # Default index if no potion is valid

            # Step 3: Binary search to find the first potion
            # such that s * potions[m] >= success
            while l <= r:
                m = (l + r) // 2

                if s * potions[m] >= success:
                    # This potion works, try to find a smaller index
                    idx = m
                    r = m - 1
                else:
                    # This potion is too weak
                    l = m + 1

            # All potions from idx to end are successful
            res.append(len(potions) - idx)

        return res
```

---

## 3. Solution Approach and Logic

### Sorting + Binary Search

This problem becomes easy if we **sort the potions**.

Once potions are sorted:

* For a fixed spell `s`, we want the **first potion** such that:

s * potion >= success

This is a classic **binary search condition**.

Steps:

1. Sort potions.
2. For each spell:

   * Use binary search to find the smallest index `idx` where the condition becomes true.
   * All potions from `idx` to the end will also be valid.

Number of successful potions:

len(potions) - idx

---

### Why Binary Search Works Here

Because potions are sorted:

If s * potions[mid] >= success:
Then all potions to the right will also work.

So we search for the **leftmost valid position**.

This turns a slow nested loop into a fast logarithmic search.

---

## 4. Time and Space Complexity

### Time Complexity

Sorting potions:
O(m log m)

Binary search for each spell:
O(n log m)

Total:
O(m log m + n log m)

This is very efficient for large inputs.

---

### Space Complexity

Extra space used:
O(1) (excluding the output array)

We only use a few variables and modify potions in-place.

---

## Most Optimal Solution

The **sorting + binary search** approach is the optimal solution for this problem.

Why it is optimal:

* Brute force is too slow: O(n * m)
* Two pointers is not possible because spells are independent
* Hashing does not help because order matters

Binary search gives the best tradeoff between speed and simplicity.

This solution scales well up to 100,000 elements and is the intended approach for interviews and competitive programming.

---

## 5. Test Cases
```python
# Test Case 1
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(Solution().successfulPairs(spells, potions, success)) # Output: [4,0,3]

# Test Case 2
spells = [3,1,2]
potions = [8,5,8]
success = 16
print(Solution().successfulPairs(spells, potions, success)) # Output: [2,0,2]
```