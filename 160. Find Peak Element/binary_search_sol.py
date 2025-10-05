# Find Peak Element
# Binary Search Solution:
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
    
# Time Complexity: O(log n), where n is the length of the input array nums. The binary search algorithm reduces the search space by half in each iteration, leading to a logarithmic time complexity.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This binary search solution efficiently finds a peak element in logarithmic time, meeting the problem's requirements.


# Test cases:
nums1 = [1, 2, 3, 1]
print(Solution().findPeakElement(nums1))  # Output: 2

nums2 = [1, 2, 1, 3, 5, 6, 4]
print(Solution().findPeakElement(nums2))  # Output: 5
