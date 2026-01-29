# Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105


# Binary Search Solution:
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and
                (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]

            leftSize = m - 1 if nums[m - 1] == nums[m] else m
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1
# Time Complexity: O(log n), where n is the number of elements in the input array. This is because we are halving the search space with each iteration of the binary search.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This binary search approach efficiently narrows down the location of the single non-duplicate element by leveraging the properties of the sorted array and the pairing of elements.


# Test Case:
nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums)) # Output: 2