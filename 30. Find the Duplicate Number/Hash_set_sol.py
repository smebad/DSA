# Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

# Hash set solution:
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
    
# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(n), where n is the length of the input list nums.
# The space complexity is O(n) because we are using a hash set to store the elements we have seen so far.
# In the worst case, we may need to store all n elements in the hash set before finding the duplicate.
# However, since the problem states that there is only one duplicate number, we will find the duplicate before reaching the end of the list.

# Test Cases:
# Test case 1:
nums = [1, 3, 4, 2, 2]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 2

# Test case 2:
nums = [3, 1, 3, 4, 2]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 3

# Test case 3:
nums = [3, 3, 3, 3, 3]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 3