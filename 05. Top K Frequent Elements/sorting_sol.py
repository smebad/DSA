# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.



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