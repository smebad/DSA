# Divide Array Into Equal Pairs - LeetCode

## Problem Explanation

The problem **Divide Array Into Equal Pairs** asks us to check whether an array can be split into pairs such that:

1. Each element belongs to exactly one pair.
2. Both elements in each pair are equal.

We are given an integer array `nums` with `2 * n` elements, meaning it always has an even number of elements. We need to determine whether we can divide it into `n` pairs of equal numbers.

### Example 1

```
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: We can divide nums into pairs (2,2), (3,3), (2,2).
```

### Example 2

```
Input: nums = [1,2,3,4]
Output: false
Explanation: It is impossible to form equal pairs with these numbers.
```

### Constraints

* `nums.length == 2 * n`
* `1 <= n <= 500`
* `1 <= nums[i] <= 500`

---

## Code with Comments

### Hash Map Solution

```python
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}  # dictionary to store frequency of each number

        for num in nums:  # count frequency of each number
            if num not in count:
                count[num] = 0
            count[num] += 1

        # check if all counts are even
        for cnt in count.values():
            if cnt % 2 == 1:  # if any number appears odd times, pairing is impossible
                return False

        return True  # if all counts are even, pairing is possible
```

### Hash Set Solution

```python
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()  # set to keep track of numbers with odd occurrences

        for num in nums:
            if num not in odd_set:
                odd_set.add(num)  # first occurrence, mark it as odd
            else:
                odd_set.remove(num)  # second occurrence, it forms a pair so remove

        return not len(odd_set)  # if set is empty, all numbers are paired
```

---

## Solution Approach and Logic

### Hash Map Approach

1. Count how many times each number appears using a dictionary.
2. If any number has an odd count, pairing is impossible.
3. Otherwise, all numbers can form pairs, so return `True`.

This approach works because pairing requires an even number of occurrences for every element.

### Hash Set Approach

1. Use a set to keep track of numbers that appear an odd number of times.
2. For each number:

   * If it's not in the set, add it (first occurrence).
   * If it's already in the set, remove it (second occurrence forms a pair).
3. In the end, if the set is empty, every number formed a pair; otherwise, return `False`.

This works because the set dynamically tracks whether a number is currently unpaired.

---

## Differences Between the Solutions

* **Hash Map**: Explicitly counts how many times each number appears. At the end, checks whether all counts are even.
* **Hash Set**: Simpler and more memory-friendly in some cases. It only keeps track of whether a number is unpaired at the moment.

Both solutions achieve the same result but with slightly different approaches:

* Hash Map focuses on **frequency counting**.
* Hash Set focuses on **pair matching while iterating**.

---

## Complexity Analysis

### Hash Map Solution

* **Time Complexity**: O(n), because we iterate through the array once and then through the frequency dictionary.
* **Space Complexity**: O(n) in the worst case (all numbers are unique).

### Hash Set Solution

* **Time Complexity**: O(n), because we iterate through the array once.
* **Space Complexity**: O(n) in the worst case (all numbers are unique and none can form a pair).

### Most Optimal Approach

Both approaches have the same **time complexity** of O(n) and **space complexity** of O(n). However:

* The **Hash Set approach** can be considered slightly more optimal in practice because it eliminates numbers from the set immediately after pairing, instead of storing full counts for all numbers.
* The **Hash Map approach** is easier to understand for beginners because it explicitly checks frequencies.

---

## Conclusion

Both solutions are efficient and solve the problem within given constraints. The Hash Map solution is more intuitive for learning, while the Hash Set solution is slightly more space-efficient in practice.
