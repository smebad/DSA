# Find First and Last Position of Element in Sorted Array
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


# Binary Search Solution:
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i

# Time Complexity: O(log n), where n is the number of elements in the input array nums. This is because we perform two binary searches, each taking O(log n) time.
# Space Complexity: O(1), since we are using a constant amount of extra space regardless of the input size.
# This binary search is efficient for finding the first and last positions of the target in a sorted array, adhering to the O(log n) runtime complexity requirement.


# Test Cases
# Test Case 1:
nums = [5, 7, 7, 8, 8, 10]
target = 8
sol = Solution()
print(sol.searchRange(nums, target))  # Output: [3, 4]

# Test Case 2:
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(sol.searchRange(nums, target))  # Output: [-1, -1]