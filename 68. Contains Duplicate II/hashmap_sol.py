# Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105


# Hash Map Solution:
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
            
        return False
    
# Time Complexity: O(n) where n is the length of the nums array.
# Space Complexity: O(n) where n is the number of distinct elements in the nums array.
# This solution uses a hash map to keep track of the indices of the elements in the nums array.


# Test Cases
# Test Case 1:
nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: True

# Test Case 2:
nums = [1,0,1,1]
k = 1
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: True

# Test Case 3:
nums = [1,2,3,1,2,3]
k = 2
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))  # Output: False
