# Brute Force Solution:

from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Test Cases
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True