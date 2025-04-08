# Longest Consecutive Sequence
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Hash map Solution:
from typing import List
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
    

# Time Complexity: O(n), where n is the number of elements in the input list nums.
# Space Complexity: O(n), for storing the elements in the hash map.

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