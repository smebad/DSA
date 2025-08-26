# Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000


# Two Pointers Solution:
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [3,1,2,4]
print(sol.sortArrayByParity(nums1))  # Output: [2,4,3,1] or any valid arrangement

# Test Case 2:
nums2 = [0]
print(sol.sortArrayByParity(nums2))  # Output: [0]