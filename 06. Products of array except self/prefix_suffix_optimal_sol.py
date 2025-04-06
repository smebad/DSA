# Products of Array Except Self
# Prefix and Suffix (optimal) Solution:
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding the output array)

# Test Cases
# Test Case 1:
nums = [1, 2, 4, 6]
print(Solution().productExceptSelf(nums))  # Output: [48, 24, 12, 8]

# Test Case 2:
nums = [-1, 0, 1, 2, 3]
print(Solution().productExceptSelf(nums))  # Output: [0, -6, 0, 0, 0]

# Test Case 3:
nums = [0, 0, 0, 0]
print(Solution().productExceptSelf(nums))  # Output: [0, 0, 0, 0]
