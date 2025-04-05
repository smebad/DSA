# Top K Frequent Elements - Leetcode Blind 75

## Problem Description
This is one of the Blind 75 LeetCode problems. Given an integer array `nums` and an integer `k`, the task is to return the `k` most frequent elements in the array. The test cases are constructed such that the answer is always unique. The output can be returned in any order.

### Examples
**Example 1:**
```
Input: nums = [1, 2, 2, 3, 3, 3], k = 2
Output: [2, 3]
```

**Example 2:**
```
Input: nums = [7, 7], k = 1
Output: [7]
```

### Constraints
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000
- 1 <= k <= number of distinct elements in nums

---

## Solution 1: Bucket Sort Approach
### Description
This solution uses a frequency dictionary to count occurrences of each number. Then it uses a list of lists (`freq`) where the index represents the frequency and the list at each index contains numbers with that frequency. It iterates this list from the highest frequency to the lowest and accumulates the most frequent elements.

### Code
```python
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```

### Time and Space Complexity
- **Time Complexity:** O(n), where n is the length of `nums`
- **Space Complexity:** O(n)

---

## Solution 2: Sorting Approach
### Description
This solution also starts by counting the frequency of each number. It then stores frequency-number pairs in an array, sorts it, and pops the top `k` elements.

### Code
```python
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
```

### Time and Space Complexity
- **Time Complexity:** O(n log n), due to sorting
- **Space Complexity:** O(n)

---

## Test Cases
```python
# Test Case 1:
nums = [1, 2, 2, 3, 3, 3]
k = 2
print(Solution().topKFrequent(nums, k))  # Output: [2, 3]

# Test Case 2:
nums = [7, 7]
k = 1
print(Solution().topKFrequent(nums, k))  # Output: [7]

# Test Case 3:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))  # Output: [1, 2]
```

---

## Summary
This problem is great for practicing frequency counting and optimizing with different data structures. The bucket sort method provides an optimal O(n) solution, while the sorting-based method is simpler but runs in O(n log n) time. Both use extra space proportional to the input size.
