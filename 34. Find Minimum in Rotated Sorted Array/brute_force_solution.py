# Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


# Brute Force Solution:
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# The brute force solution is to simply find the minimum element in the array using the built-in min function. This approach has a time complexity of O(n) because it needs to iterate through all elements in the array to find the minimum. The space complexity is O(1) since we are not using any additional data structures that grow with the input size.
# However, this approach does not meet the requirement of O(log n) time complexity.
# To achieve O(log n) time complexity, we can use a binary search approach. The idea is to find the pivot point where the array is rotated and then return the minimum element based on the pivot point. This approach has a time complexity of O(log n) and a space complexity of O(1).


# Test Cases:
# Test Case 1:
nums = [3,4,5,1,2]
sol = Solution()
print(sol.findMin(nums))  # Output: 1

# Test Case 2:
nums = [4,5,6,7,0,1,2]
sol = Solution()
print(sol.findMin(nums))  # Output: 0

# Test Case 3:
nums = [11,13,15,17]
sol = Solution()
print(sol.findMin(nums))  # Output: 11