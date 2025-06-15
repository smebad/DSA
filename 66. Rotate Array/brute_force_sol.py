# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


# Brute Force Solution:
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        while k:
            tmp = nums[n - 1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = tmp
            k -= 1

# Time Complexity: O(n * k) where n * k means the number of times we need to rotate the array. This is because we need to iterate through the array k times to rotate it.
# Space Complexity: O(1) in this brute force solution as we are not using any extra space. how it works is that we are simply rotating the array k times.
# This solution is not efficient for large inputs as it has a time complexity of O(n * k). 


# Test Cases:
# Test Case 1
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums) # Expected Output: [5,6,7,1,2,3,4]

# Test Case 2
nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
print(nums) # Expected Output: [3,99,-1,-100]