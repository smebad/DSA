# Maximum Width Ramp
# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

# Example 1:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:

# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

# Constraints:

# 2 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5 * 104


# Sliding Window Solution:
from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0

        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i -= 1

        res = 0
        l = 0

        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            res = max(res, r - l)
        
        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array a constant number of times.
# Space Complexity: O(n), due to the additional array max_right used to store the maximum values from the right side of the array.
# This sliding window approach efficiently finds the maximum width ramp by leveraging precomputed maximums.


# Test Cases:
# Test Case 1:
nums1 = [6,0,8,2,1,5]
print(Solution().maxWidthRamp(nums1)) # 4

# Test Case 2:
nums2 = [9,8,1,0,1,9,4,0,4,1]
print(Solution().maxWidthRamp(nums2)) # 7