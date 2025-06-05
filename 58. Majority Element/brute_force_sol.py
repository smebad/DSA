# Majority Element
# Brute Force Solution:

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n // 2:
                return num
    
# Time Complexity: O(n^2) where n is the length of nums because we iterate over nums twice.
# Space Complexity: O(1) this is because we are not using any additional space.
# Brute force solution is not optimal for large inputs as it takes O(n^2) time complexity


# Test Cases:
# Test Case 1:
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))  # Output: 3

# Test Case 2:
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))  # Output: 2

