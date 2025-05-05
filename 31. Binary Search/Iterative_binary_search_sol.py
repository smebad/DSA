# Binary Search
# Iterative Binary Search solution:

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)  

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
    
# Time complexity: O(log n) where n is the length of nums
# Space complexity: O(1) since we are not using any extra space apart from the variables l and r and m.
# This iterative binary search solution is efficient and works well for large input sizes.
# The use of (l + (r - l) // 2) instead of (l + r) // 2 prevents overflow in languages with fixed integer sizes, but in Python, this is not a concern since integers can grow arbitrarily large.
# However, it's still a good practice to use the former approach for better readability and to avoid potential issues in other languages.


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
