# Find Pivot Index
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

