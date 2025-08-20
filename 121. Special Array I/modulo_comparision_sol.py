# Special Array I
# An array is considered special if the parity of every pair of adjacent elements is different. In other words, one element in each pair must be even, and the other must be odd.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 

# Example 1:

# Input: nums = [1]

# Output: true

# Explanation:

# There is only one element. So the answer is true.

# Example 2:

# Input: nums = [2,1,4]

# Output: true

# Explanation:

# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

# Example 3:

# Input: nums = [4,3,1,6]

# Output: false

# Explanation:

# nums[1] and nums[2] are both odd. So the answer is false.

 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# Modulo Comparison Solution:
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return True
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to check the parity of adjacent elements.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# In this modulo comparison solution, we utilize the properties of even and odd numbers by checking the remainder when divided by 2. This allows us to efficiently determine if the array is special. 

# Test Cases
# Test Case 1:
nums1 = [1]
print(Solution().isArraySpecial(nums1))  # Expected output: True

# Test Case 2:
nums2 = [2, 1, 4]
print(Solution().isArraySpecial(nums2))  # Expected output: True

# Test Case 3:
nums3 = [4, 3, 1, 6]
print(Solution().isArraySpecial(nums3))  # Expected output: False
