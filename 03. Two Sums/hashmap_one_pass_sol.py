# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000


# Hashmap one pass Solution:
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i
    
# Time Complexity: O(n)
# Space Complexity: O(n)


# Test Cases
# Test Case 1:
sol = Solution()
nums = [3, 4, 5, 6]
target = 7
print(sol.twoSum(nums, target))  # Output: [0, 1]

# Test Case 2:
nums = [4, 5, 6]
target = 10
print(sol.twoSum(nums, target))  # Output: [0, 2]