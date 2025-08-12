# Find Pivot Index
# Prefix-Sum Solution:
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
    
# Time Complexity: O(n), where n is the length of the input list nums. We calculate the total sum in O(n) time and then iterate through the list once to find the pivot index.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This prefix-sum solution is more efficient than the brute-force solution, especially for large input sizes.



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

