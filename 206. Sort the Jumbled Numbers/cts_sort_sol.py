# Sort the Jumbled Numbers
# Convert to strings + sorting solution:
from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i, n in enumerate(nums):
            n = str(n)
            mapped_n = 0
            for c in n:
                mapped_n *= 10
                mapped_n += mapping[int(c)]
            pairs.append((mapped_n, i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]
  
# Time Complexity: O(n log n), where n is the number of elements in nums. This is due to the sorting step.
# Space Complexity: O(n), for storing the pairs of mapped values and original indices.
# This convert to strings + sorting solution effectively maps each number according to the given mapping and sorts them while maintaining the original order for numbers with the same mapped value.


# Test cases
sol = Solution()

# Test Case 1:
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
print(sol.sortJumbled(mapping, nums))  # Expected Output: [338, 38, 991]

# Test Case 2:
mapping = [0,1,2,3,4,5,6,7,8,9]
nums = [789,456,123]
print(sol.sortJumbled(mapping, nums))  # Expected Output: [123, 456, 789]
