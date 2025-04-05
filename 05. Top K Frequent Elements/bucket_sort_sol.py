# Top K Frequent Elements
# Bucket Sort Solution (Optimal)
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
                
# Time complexity: O(n)
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
