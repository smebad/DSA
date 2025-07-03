# Search in Rotated Sorted Array II
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104
 

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?


# Binary Search Solution:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True

            if nums[l] < nums[m]:  # Left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:  # Right portion
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False
    
# Time Complexity: O(log n) in average case, O(n) in worst case due to duplicates. This is because we may have to check every element in the worst case when all elements are the same and the target is not present.
# Space Complexity: O(1) since we are using a constant amount of space regardless of the input size. This is because we are only using a few variables to keep track of indices and the target value.
# This solution is efficient for the problem constraints and handles duplicates effectively by adjusting the search range when duplicates are encountered.


# Test Case
# Test Case 1:
nums = [2,5,6,0,0,1,2]
target = 0
print(Solution().search(nums, target)) # Expected Output: True

# Test Case 2:
nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums, target)) # Expected Output: False