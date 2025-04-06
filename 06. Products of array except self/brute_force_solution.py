# Products of Array Except Self
# Solved 
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

# Brute Force Solution:
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res
    
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding the output array)

# Test Cases
# Test Case 1:
nums = [1, 2, 4, 6]
print(Solution().productExceptSelf(nums))  # Output: [48, 24, 12, 8]

# Test Case 2:
nums = [-1, 0, 1, 2, 3]
print(Solution().productExceptSelf(nums))  # Output: [0, -6, 0, 0, 0]

# Test Case 3:
nums = [0, 0, 0, 0]
print(Solution().productExceptSelf(nums))  # Output: [0, 0, 0, 0]