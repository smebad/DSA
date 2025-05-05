# Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Upper bound solution:
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1
    
# Time complexity: O(log n) where n is the length of nums
# Space complexity: O(1) since we are not using any extra space apart from the variables l and r and m.
# This upper bound binary search solution is also efficient as compared to the lower bound solution. The difference in both lower and upper bound solutions is the condition used in the while loop and the return statement.
# However, both solutions have the same time and space complexity.
# The upper bound solution is useful when we want to find the last occurrence of the target in the array, while the lower bound solution is useful when we want to find the first occurrence of the target.


# Test Cases:
# Test Case 1:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
print(sol.search(nums, target))  # Output: 4

# Test Case 2:
nums = [-1, 0, 3, 5, 9, 12]
target = 2
sol = Solution()
print(sol.search(nums, target))  # Output: -1

# Test Case 3:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
sol = Solution()
print(sol.search(nums, target))  # Output: 4