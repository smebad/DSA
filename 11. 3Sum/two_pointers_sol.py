# 15. 3Sum
# Attempted
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Two Pointers Solution:
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
    
# Time Complexity: O(n^2) where n is the number of elements in the input list. The two pointers approach reduces the time complexity significantly compared to the brute force approach.
# Space Complexity: O(1) for the two pointers approach as we are not using any extra space apart from the result list. The result list can take O(m) space where m is the number of unique triplets found.
# This is a more efficient solution compared to the brute force approach.

# Test Cases:
# Test Case 1:
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums)) # Expected Output: [[-1,-1,2],[-1,0,1]]

# Test Case 2:
nums = [0,1,1]
print(Solution().threeSum(nums)) # Expected Output: []

# Test Case 3:
nums = [0,0,0]
print(Solution().threeSum(nums)) # Expected Output: [[0,0,0]]