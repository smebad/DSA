# Solution:

from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# Test Cases
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
