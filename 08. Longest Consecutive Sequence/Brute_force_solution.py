# Longest Consecutive Sequence
# Brute Force Solution:
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
    

# Time Complexity: O(n^2) in the worst case, where n is the length of the input list nums.
# Space Complexity: O(n) for the set store.

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
