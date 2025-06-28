# Search Insert Position
# Linear Search Solution:

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
# Time Complexity: O(n) where n is the length of the input list nums. This is because in the worst case, we may have to iterate through the entire list to find the target or determine where it should be inserted.
# Space Complexity: O(1) since we are using a constant amount of space regardless of the input size.
# This solution is only optimal for small input sizes. For larger inputs, a binary search solution would be more efficient with O(log n) time complexity.


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
