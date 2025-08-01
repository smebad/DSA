# Binary Search
# Lower bound solution:

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1
    
# Time complexity: O(log n) where n is the length of nums
# Space complexity: O(1) since we are not using any extra space apart from the variables l and r and m.
# This lower bound binary search solution is efficient and works well for large input sizes.


# Test Cases:
# Test Case 1:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
print(sol.search(nums, target))  # Output: 4

# Test Case 2:
nums = [-1, 0, 3, 5, 9, 12]
target = 2
sol = Solution()
print(sol.search(nums, target))  # Output: -1

# Test Case 3:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
sol = Solution()
print(sol.search(nums, target))  # Output: 4
