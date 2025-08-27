# Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105


# One Pass Solution:
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase, decrease = True, True

        for i in range(len(nums) - 1):
            if not (nums[i] <= nums[i + 1]):
                increase = False
            if not (nums[i] >= nums[i + 1]):
                decrease = False
        return increase or decrease

# Time Complexity: O(n), where n is the length of the input array. In this solution, we traverse the array only once.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This one-pass solution is efficient and works well within the given constraints.


# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [1, 2, 2, 3]
print(sol.isMonotonic(nums1))  # Output: True

# Test Case 2:
nums2 = [6, 5, 4, 4]
print(sol.isMonotonic(nums2))  # Output: True

# Test Case 3:
nums3 = [1, 3, 2]
print(sol.isMonotonic(nums3))  # Output: False
