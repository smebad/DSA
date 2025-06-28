# Search Insert Position
# Binary Search Solution:

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
    
# Time Complexity: O(log n) where n is the length of the input list nums. This is because we are using binary search, which divides the search space in half with each iteration.
# Space Complexity: O(1) since we are using a constant amount of space regardless of the input size.
# This solution is optimal for large input sizes due to its logarithmic time complexity.

# Test Cases
# Test Case 1:
nums1 = [1, 3, 5, 6]
target1 = 5
print(Solution().searchInsert(nums1, target1))  # Output: 2

# Test Case 2:
nums2 = [1, 3, 5, 6]
target2 = 2
print(Solution().searchInsert(nums2, target2))  # Output: 1

# Test Case 3:
nums3 = [1, 3, 5, 6]
target3 = 7
print(Solution().searchInsert(nums3, target3))  # Output: 4
