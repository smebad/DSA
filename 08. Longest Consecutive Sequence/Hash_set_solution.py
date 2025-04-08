# Longest Consecutive Sequence
# Hash set Solution:
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(n) for the set numSet.

# Test Cases:
# Test Case 1:
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums)) # Output: 4

# Test Case 2:
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums)) # Output: 9

# Test Case 3:
nums = [1,0,1,2]
print(Solution().longestConsecutive(nums)) # Output: 3
