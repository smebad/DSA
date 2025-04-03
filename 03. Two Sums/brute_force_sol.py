# Two Sum
# Brute Force Solution:
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)


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
