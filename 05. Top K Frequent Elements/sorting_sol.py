# Top K Frequent Elements
# Sorting solution (not the optimal one)
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
                
# Time complexity: O(n log n)
# Space complexity: O(n)

# Test cases
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
