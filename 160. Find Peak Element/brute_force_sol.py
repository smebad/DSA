# Find Peak Element
# Brute Force Solution:
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1
    
# Time Complexity: O(n), where n is the length of the input array nums. In the worst case, we may need to traverse the entire array to find a peak element.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This brute force solution is straightforward and easy to understand, but it does not meet the O(log n) time complexity requirement specified in the problem statement.


# Test cases:
nums1 = [1, 2, 3, 1]
print(Solution().findPeakElement(nums1))  # Output: 2

nums2 = [1, 2, 1, 3, 5, 6, 4]
print(Solution().findPeakElement(nums2))  # Output: 5
