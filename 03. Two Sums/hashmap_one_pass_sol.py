# Two Sum
# Hashmap one pass Solution:
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i
    
# Time Complexity: O(n)
# Space Complexity: O(n)


# Test Cases
# Test Case 1:
sol = Solution()
nums = [3, 4, 5, 6]
target = 7
print(sol.twoSum(nums, target))  # Output: [0, 1]

# Test Case 2:
nums = [4, 5, 6]
target = 10
print(sol.twoSum(nums, target))  # Output: [0, 2]
