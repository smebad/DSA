# Majority Element
# Sorting Solution:
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
# Time Complexity: O(n log n) where n is the length of nums because we sort the array.
# Space Complexity: O(1) this is because we are not using any additional space.
# Sorting solution is not optimal for large inputs as it takes O(n log n) time complexity
# However it is a good solution for small inputs


# Test Cases:
# Test Case 1:
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))  # Output: 3

# Test Case 2:
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))  # Output: 2

