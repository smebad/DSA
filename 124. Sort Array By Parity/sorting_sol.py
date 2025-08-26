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


# Sorting Solution:
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: x & 1)
        return nums
    
# Time Complexity: O(n log n) due to the sorting operation. This is because sorting takes O(n log n) time in the worst case.
# Space Complexity: O(1) or O(n) depending on the sorting algorithm used.
# This sorting approach is not optimal for this problem since we only need to partition the array into evens and odds.


# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [3,1,2,4]
print(sol.sortArrayByParity(nums1))  # Output: [2,4,3,1] or any valid arrangement

# Test Case 2:
nums2 = [0]
print(sol.sortArrayByParity(nums2))  # Output: [0]