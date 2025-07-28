# Find Lucky Integer in an Array - LeetCode

## Problem Explanation

A **lucky integer** in an array is an integer that appears in the array exactly as many times as its value. Your task is to find the **largest lucky integer**. If there are no lucky integers, return `-1`.

### Examples:

1. Input: `[2,2,3,4]` → Output: `2` (because 2 appears twice)
2. Input: `[1,2,2,3,3,3]` → Output: `3` (1 appears once, 2 appears twice, 3 appears three times)
3. Input: `[2,2,2,3,3]` → Output: `-1` (no number matches its frequency)

---

## Constraints:

* `1 <= arr.length <= 500`
* `1 <= arr[i] <= 500`

## Brute Force Solution

```python
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1  # initialize result as -1 (no lucky integer)

        for num in arr:  # iterate over each element
            cnt = 0
            for a in arr:  # count occurrences of the current number
                if num == a:
                    cnt += 1
            if cnt == num:  # check if frequency equals its value
                res = max(res, num)  # keep track of the largest lucky number

        return res  # return result
```

### Explanation:

* Loop over each number and count its occurrences.
* If the count equals the number itself, it's a lucky integer.
* Track the maximum such integer.

### Time Complexity: `O(n^2)`

* Two nested loops to count frequencies.

### Space Complexity: `O(1)`

* Only a few variables used.

---

## Sorting-Based Solution

```python
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()  # sort the array to group equal numbers
        streak = 0
        for i in range(len(arr) - 1, -1, -1):  # traverse from right to left
            streak += 1  # count frequency
            if i == 0 or arr[i] != arr[i - 1]:  # check end of group
                if arr[i] == streak:  # lucky number condition
                    return arr[i]  # return the largest one first (due to reverse loop)
                streak = 0  # reset for next number group
        return -1  # no lucky number found
```

### Explanation:

* Sort array and iterate backwards.
* Count frequency using `streak`, reset when number changes.
* Return the largest number that matches its frequency.

### Time Complexity: `O(n log n)`

* Due to sorting.

### Space Complexity: `O(1)`

* Only a counter used.

---

## Hash Map (Optimal) Solution

```python
from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)  # count frequencies using hash map
        res = -1

        for num in cnt:  # iterate over keys (unique numbers)
            if num == cnt[num]:  # check if value equals frequency
                res = max(num, res)  # store max lucky number found

        return res
```

### Explanation:

* Use `collections.Counter` to count occurrences efficiently.
* Loop through key-value pairs to find lucky integers.
* Track the largest such number.

### Time Complexity: `O(n)`

* One pass for counting and one pass for checking.

### Space Complexity: `O(n)`

* Stores frequency of each number.

---

## Comparison of All Solutions

| Approach      | Time Complexity | Space Complexity | Optimal? | Notes                            |
| ------------- | --------------- | ---------------- | -------- | -------------------------------- |
| Brute Force   | O(n^2)          | O(1)             | No       | Slow for larger arrays           |
| Sorting-Based | O(n log n)      | O(1)             | Yes      | Better, avoids hash map          |
| Hash Map      | O(n)            | O(n)             | Yes      | Fastest, best for large datasets |

### Most Optimal:

The **Hash Map solution** is optimal in terms of time complexity, especially for larger arrays. However, if memory is a concern and the array is small, the **sorting-based** approach might be preferable due to its constant space usage.

---

## Test Cases

```python
# Test Case 1:
solution = Solution()
arr = [2, 2, 3, 4]
print(solution.findLucky(arr))  # Output: 2

# Test Case 2:
arr = [1, 2, 2, 3, 3, 3]
print(solution.findLucky(arr))  # Output: 3

# Test Case 3:
arr = [2, 2, 2, 3, 3]
print(solution.findLucky(arr))  # Output: -1
```