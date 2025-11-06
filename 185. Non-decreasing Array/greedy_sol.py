# Non-decreasing Array
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105


# Greedy Solution:
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(1), as we use only a constant amount of extra space.
# This greedy solution is efficient and effectively checks if the array can be made non-decreasing by modifying at most one element.


# Test Cases:
sol = Solution()

# Test Case 1
print(sol.checkPossibility([4, 2, 3]))  # Expected output: True

# Test Case 2
print(sol.checkPossibility([4, 2, 1]))  # Expected output: False