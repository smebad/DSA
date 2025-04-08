# Longest Consecutive Sequence - LeetCode (Blind 75)

## Problem Description
Given an unsorted array of integers `nums`, return the length of the **longest consecutive elements sequence**.

The algorithm must run in **O(n)** time.

### Examples
**Example 1:**
```
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].
```

**Example 2:**
```
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
```

**Example 3:**
```
Input: nums = [1, 0, 1, 2]
Output: 3
```

### Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

---

## What is the Longest Consecutive Sequence Problem?
The task is to find the **maximum length** of a sequence of **consecutive integers** (i.e., numbers that come one after another) from an **unsorted** list. The key challenge is achieving this in **linear time**, rather than sorting the array which would take O(n log n).

---

## Solution 1: Brute Force
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
```

### Explanation
1. Convert the list to a set to allow O(1) lookups.
2. For every number in the original list, try to build a consecutive sequence starting from that number.
3. Keep track of the maximum sequence length.

### Time Complexity: O(n^2)
In the worst case, for every number we may end up scanning the entire sequence again and again.

### Space Complexity: O(n)
To store the numbers in a set.

---

## Solution 2: Hash Map Optimization
```python
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
```

### Explanation
This method uses a hash map to dynamically track and merge sequences.
- If a number is already used, skip it.
- Otherwise, it checks left and right streaks and connects them.
- The boundaries of the merged streak are updated accordingly.

### Time Complexity: O(n)
Each number is only processed once.

### Space Complexity: O(n)
For the hash map.

---

## Solution 3: Hash Set (Most Optimal)
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```

### Explanation (Step-by-Step):
1. Add all numbers to a set for O(1) lookups.
2. For each number, check if it is the **start** of a sequence (i.e., `num - 1` is not in the set).
3. If so, count forward until the sequence breaks.
4. Track the maximum length encountered.

### Time Complexity: O(n)
Each number is visited at most once.

### Space Complexity: O(n)
For the set used for fast lookup.

---

## Summary
| Solution           | Time Complexity | Space Complexity | Description                              |
|--------------------|------------------|-------------------|------------------------------------------|
| Brute Force        | O(n^2)           | O(n)              | Checks all possible sequences repeatedly |
| Hash Map           | O(n)             | O(n)              | Merges sequences using map boundaries    |
| Hash Set (Optimal) | O(n)             | O(n)              | Efficiently finds sequence starts only   |

**Most Optimal Solution:** The Hash Set approach is the cleanest and most efficient, adhering to the required O(n) time constraint with a straightforward implementation.