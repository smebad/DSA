# Search in Rotated Sorted Array
# Brute Force Solution:

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
# Time Complexity: O(n) because we are iterating through the entire list in the worst case
# Space Complexity: O(1) because we are not using any additional data structures
# This is a brute force solution and not optimal for large inputs but it is easy to understand and implement.
# The optimal solution is to use binary search which has a time complexity of O(log n) and is more efficient for large inputs.


# Test Cases:
# Test Case 1: 
nums = [4,5,6,7,0,1,2] 
target = 0
print(Solution().search(nums, target)) # Output: 4

# Test Case 2:
nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums, target)) # Output: -1

# Test Case 3:
nums = [1]
target = 0
print(Solution().search(nums, target)) # Output: -1
