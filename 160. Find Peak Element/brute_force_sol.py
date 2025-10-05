# Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.


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