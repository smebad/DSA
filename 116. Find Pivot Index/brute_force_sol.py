# Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

# Constraints:

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


# Brute-Force Solution:
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            leftSum = rightSum = 0
            for l in range(i):
                leftSum += nums[l]
            for r in range(i + 1, n):
                rightSum += nums[r]
            if leftSum == rightSum:
                return i
        return -1
    
# Time Complexity: O(n^2), where n is the length of the input list nums. The outer loop iterates through all possible pivot indices, and the inner loops calculate the left and right sums for each pivot index, which takes O(n) time.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This brute-force solution is not optimal for large input sizes due to its quadratic time complexity.


# Test Cases
solution = Solution()
# Test Case 1:
nums1 = [1, 7, 3, 6, 5, 6]
print(solution.pivotIndex(nums1))  # Output: 3

# Test Case 2:
nums2 = [1, 2, 3]
print(solution.pivotIndex(nums2))  # Output: -1

# Test Case 3:
nums3 = [2, 1, -1]
print(solution.pivotIndex(nums3))  # Output: 0
