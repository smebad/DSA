# Subarray Sum Equals K - LeetCode

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of **subarrays** whose sum is equal to `k`.

A **subarray** is a contiguous (consecutive) non-empty sequence of elements within an array.

### Example 1:

**Input:** nums = \[1,1,1], k = 2
**Output:** 2

### Example 2:

**Input:** nums = \[1,2,3], k = 3
**Output:** 2

### Constraints:

* 1 <= nums.length <= 20,000
* -1000 <= nums\[i] <= 1000
* -10^7 <= k <= 10^7

---

## Code and Explanation

### Hash Map Solution

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }  # Dictionary to store frequency of prefix sums

        for num in nums:
            curSum += num  # Update running prefix sum
            diff = curSum - k  # We want to know if there is a prefix sum that when removed results in k

            res += prefixSums.get(diff, 0)  # If such a prefix sum exists, add its frequency to result
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)  # Update prefix sum frequency
        
        return res
```

### How it Works:

* A prefix sum is the sum of elements from the beginning of the array to the current index.
* To find the number of subarrays that sum to `k`, we track all prefix sums we've seen.
* If `curSum - k` exists in our prefix sums map, it means there's a subarray ending at the current index which sums to `k`.
* This is because `curSum - (curSum - k) = k`.

### Test Cases:

```python
# Test Case 1:
nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))  # Output: 2

# Test Case 2:
nums = [1,2,3]
k = 3
sol = Solution()
print(sol.subarraySum(nums, k))  # Output: 2
```

---

## Time and Space Complexity

### Time Complexity: `O(n)`

* We traverse the array only once, doing constant time operations at each step.

### Space Complexity: `O(n)`

* In the worst case, the dictionary may store up to `n` different prefix sums.

---

## Why This Solution is Optimal

* **Most Efficient Time:** Linear time solution makes it suitable for large inputs (up to 20,000 elements).
* **Space Usage is Justified:** The hashmap used for prefix sums is crucial for keeping the solution linear. It's a space-time tradeoff, but necessary for speed.

---

## Summary

This problem is best solved using the prefix sum + hashmap approach. It allows us to count subarrays with a specific sum in `O(n)` time without explicitly checking all possible subarrays (which would be `O(n^2)` in brute force).

Understanding the prefix sum concept and how past sums can help us detect valid subarrays is key to mastering problems like this.
