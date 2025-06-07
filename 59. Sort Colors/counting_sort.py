# Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


# Counting Sort Solution:
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

# Time Complexity: O(n) where n is the length of nums array. This is because we iterate through the array once to count the frequency of each color, and then we iterate through the array again to place the colors in the correct order.
# Space Complexity: O(1) since we only use a constant amount of extra space to store the count array.
# Thiscounting sort solution is a good solution for small inputs as it takes O(n) time complexity.


# Test Cases:
# Test Case 1
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums) # Output: [0,0,1,1,2,2]

# Test Case 2
nums = [2,0,1]
Solution().sortColors(nums)
print(nums) # Output: [0,1,2]
