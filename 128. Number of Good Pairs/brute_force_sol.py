# Number of Good Pairs
# Brute Force Solution:
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res

# Time Complexity: O(n^2), where n is the length of the input array. In this case, we are using a brute force approach to check all possible pairs.
# Space Complexity: O(1), we are using a constant amount of space.
# This solution is not optimal for large input sizes, and a more efficient approach could be considered.

# Test Cases
sol = Solution()

# Test Case 1:
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums))  # Output: 4

# Test Case 2:
nums = [1,1,1,1]
print(sol.numIdenticalPairs(nums))  # Output: 6

# Test Case 3:
nums = [1,2,3]
print(sol.numIdenticalPairs(nums))  # Output: 0

