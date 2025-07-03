# Search in Rotated Sorted Array II
# Binary Search Solution:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True

            if nums[l] < nums[m]:  # Left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:  # Right portion
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False
    
# Time Complexity: O(log n) in average case, O(n) in worst case due to duplicates. This is because we may have to check every element in the worst case when all elements are the same and the target is not present.
# Space Complexity: O(1) since we are using a constant amount of space regardless of the input size. This is because we are only using a few variables to keep track of indices and the target value.
# This solution is efficient for the problem constraints and handles duplicates effectively by adjusting the search range when duplicates are encountered.


# Test Case
# Test Case 1:
nums = [2,5,6,0,0,1,2]
target = 0
print(Solution().search(nums, target)) # Expected Output: True

# Test Case 2:
nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums, target)) # Expected Output: False
