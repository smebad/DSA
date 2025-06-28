# Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


# Linear Search Solution:
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
# Time Complexity: O(n) where n is the length of the input list nums. This is because in the worst case, we may have to iterate through the entire list to find the target or determine where it should be inserted.
# Space Complexity: O(1) since we are using a constant amount of space regardless of the input size.
# This solution is only optimal for small input sizes. For larger inputs, a binary search solution would be more efficient with O(log n) time complexity.


# Test Cases
# Test Case 1:
nums1 = [1, 3, 5, 6]
target1 = 5
print(Solution().searchInsert(nums1, target1))  # Output: 2

# Test Case 2:
nums2 = [1, 3, 5, 6]
target2 = 2
print(Solution().searchInsert(nums2, target2))  # Output: 1

# Test Case 3:
nums3 = [1, 3, 5, 6]
target3 = 7
print(Solution().searchInsert(nums3, target3))  # Output: 4