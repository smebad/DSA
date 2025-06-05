# Majority Element
# Hash Map Solution:
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res
    
# Time Complexity: O(n) where n is the length of nums because we iterate over nums once.
# Space Complexity: O(n) where n is the length of nums because we create a dictionary of size n.


# Test Cases:
# Test Case 1:
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))  # Output: 3

# Test Case 2:
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))  # Output: 2

