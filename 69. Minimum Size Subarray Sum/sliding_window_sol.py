# Minimum Size Subarray Sum
# 209. Minimum Size Subarray Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Sliding Window Solution:
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res
    
# Time Complexity: O(n) where n is the length of the array. This is because we need to iterate through the array once to find the minimum subarray length.
# Space Complexity: O(1) this is because we are using only a constant amount of space for the pointers l and r.
# This sliding window solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases
# Test Case 1:
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums)) # Expected Output: 2

# Test Case 2:
target = 4
nums = [1,4,4]
print(Solution().minSubArrayLen(target, nums)) # Expected Output: 1

# Test Case 3:
target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums)) # Expected Output: 0
