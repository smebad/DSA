# Single Element in a Sorted Array
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
