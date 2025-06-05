# Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?


# Hash Map Solution:
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
# Time Complexity: O(n log n) where n is the length of nums because we sort the array.
# Space Complexity: O(1) this is because we are not using any additional space.
# Sorting solution is not optimal for large inputs as it takes O(n log n) time complexity
# However it is a good solution for small inputs


# Test Cases:
# Test Case 1:
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))  # Output: 3

# Test Case 2:
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))  # Output: 2

