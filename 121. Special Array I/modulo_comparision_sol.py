# Special Array I
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

