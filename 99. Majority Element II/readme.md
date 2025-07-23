# Majority Element II - LeetCode

## Problem Statement

Given an integer array `nums` of size `n`, the task is to find all elements that appear more than `n / 3` times.

### Example 1:

```
Input: nums = [3,2,3]
Output: [3]
```

### Example 2:

```
Input: nums = [1]
Output: [1]
```

### Example 3:

```
Input: nums = [1,2]
Output: [1,2]
```

### Constraints:

* 1 <= nums.length <= 5 \* 10^4
* -10^9 <= nums\[i] <= 10^9

### Follow-up:

Can you solve the problem in linear time and O(1) space?

---

## Hashmap-Based Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        
        # Count potential candidates using reduction logic
        for num in nums:
            count[num] += 1
            
            # Reduce the size of hashmap if it grows beyond 2
            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count
        
        # Verify if potential candidates actually appear > n/3 times
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
```

### Explanation:

* First, we use a dictionary (`count`) to track counts.
* If there are more than 2 distinct elements, we decrement their counts and prune those with zero count.
* This simulates a variation of the **Boyer-Moore Voting Algorithm**.
* At the end, we validate the remaining candidates to ensure they actually appear more than `n / 3` times.

### Time and Space Complexity:

* **Time:** O(n) for scanning the array + O(n) for validating candidates = O(n)
* **Space:** O(1), as the hashmap only holds at most 2 candidates.

---

## Sorting-Based Solution

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res, n = [], len(nums)
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            if (j - i) > n // 3:
                res.append(nums[i])
            i = j
        return res
```

### Explanation:

* First, we sort the array so that all duplicates are adjacent.
* We count the frequency of each distinct element using two pointers.
* If the count exceeds `n / 3`, we add it to the result list.

### Time and Space Complexity:

* **Time:** O(n log n) due to sorting.
* **Space:** O(1), if we exclude the output list.

---

## Summary of Approaches

| Approach          | Time Complexity | Space Complexity | Description                                           |
| ----------------- | --------------- | ---------------- | ----------------------------------------------------- |
| Hashmap/Reduction | O(n)            | O(1)             | Efficient, uses modified Boyer-Moore Voting algorithm |
| Sorting           | O(n log n)      | O(1)             | Simple, but not optimal in time                       |

### Optimal Solution:

The **hashmap-based reduction approach** is optimal as it solves the problem in linear time `O(n)` and constant space `O(1)` (excluding the result). It uses a reduction technique that limits potential candidates to at most 2 elements (as at most two elements can occur more than n/3 times).

This approach is ideal for large input sizes and follows a strategy similar to the Boyer-Moore Voting Algorithm used in the original Majority Element problem (n/2 version).