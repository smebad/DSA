# Sort Array By Parity
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

# Time Complexity: O(n), where n is the length of the input array. We make a single pass through the array.
# Space Complexity: O(1), since we are sorting the array in place and using only a constant amount of extra space.
# This two pointers approach is optimal for this problem.

# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [3,1,2,4]
print(sol.sortArrayByParity(nums1))  # Output: [2,4,3,1] or any valid arrangement

# Test Case 2:
nums2 = [0]

print(sol.sortArrayByParity(nums2))  # Output: [0]
