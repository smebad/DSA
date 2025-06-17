# Contains Duplicate II - LeetCode

## Problem Description

The **Contains Duplicate II** problem requires us to determine whether any value appears **at least twice** in an array **such that the two indices are at most `k` distance apart**.

### Given:

* An integer array `nums`
* An integer `k`

### Task:

Return `True` if there are two distinct indices `i` and `j` in the array such that:

* `nums[i] == nums[j]` and
* `abs(i - j) <= k`

---

## Example

* Input: `nums = [1,2,3,1]`, `k = 3`

  * Output: `True`
  * Because `nums[0] == nums[3]` and `|0 - 3| = 3`

* Input: `nums = [1,0,1,1]`, `k = 1`

  * Output: `True`
  * Because `nums[2] == nums[3]` and `|2 - 3| = 1`

* Input: `nums = [1,2,3,1,2,3]`, `k = 2`

  * Output: `False`
  * No such pair exists within distance 2

---

## Solution 1: Hash Map Approach

```python
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}  # Dictionary to store element and its latest index

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True  # Found a duplicate within the allowed range
            mp[nums[i]] = i  # Update index of the current element

        return False  # No valid duplicate found
```

### Explanation (Commented)

* A hash map `mp` stores the latest index of each element.
* On each iteration, if `nums[i]` is already in the map and the distance is `<= k`, we return `True`.
* Otherwise, we update the index of `nums[i]` in the map.

---

## Solution 2: Hash Set Sliding Window Approach

```python
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # A sliding window set
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])  # Slide the window
                L += 1

            if nums[R] in window:
                return True  # Found duplicate in the current window

            window.add(nums[R])  # Add current number to the window

        return False  # No duplicate found within range
```

### Explanation (Commented)

* Use a sliding window of size `k` with a hash set.
* If the element is already in the set during the sliding, return `True`.
* Otherwise, maintain the size of the window by removing the leftmost value when it exceeds `k`.

---

## Time and Space Complexities

### Hash Map Solution:

* **Time Complexity**: `O(n)` - We scan through the array once.
* **Space Complexity**: `O(n)` - In the worst case, all elements are unique.

### Hash Set Sliding Window Solution:

* **Time Complexity**: `O(n)` - We process each element once.
* **Space Complexity**: `O(min(n, k))` - The set stores at most `k` elements at any time.

---

## Optimal Solution and Why

The **Hash Set Sliding Window** solution is more optimal in terms of space because it ensures that the set never grows beyond `k` elements. This makes it a better choice when `k` is significantly smaller than `n`.

It is especially efficient when the input size is large, as it limits memory usage while maintaining linear time complexity.

---

## Test Cases

```python
# Test Case 1:
nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))  # True

# Test Case 2:
nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))  # True

# Test Case 3:
nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))  # False
```

---

## Final Notes

* Using a **Hash Map** is simple and works well in most scenarios.
* The **Sliding Window Hash Set** solution is slightly more advanced but uses less space.
* Both are efficient and acceptable in coding interviews or production environments.
