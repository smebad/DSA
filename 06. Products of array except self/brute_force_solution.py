# Products of Array Except Self
# Brute Force Solution:
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res
    
# Time Complexity: O(n^2)
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
