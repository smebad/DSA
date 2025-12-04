# Find Polygon With the Largest Perimeter
# Sorting solution:
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        total = 0
        for num in nums:
            if total > num:
                res = total + num
            total += num
        return res

# Time Complexity: O(n log n), where n is the length of nums, due to the sorting step.
# Space Complexity: O(1), as we are using a constant amount of extra space for variables or O(n) if we consider the input list as additional space.
# This sorting solution efficiently finds the largest perimeter of a polygon that can be formed from the given side lengths in nums.


# Test Cases
# Test Case 1:
nums = [5,5,5]
sol = Solution()
print(sol.largestPerimeter(nums))  # Output: 15

# Test Case 2:
nums = [1,12,1,2,5,50,3]
print(sol.largestPerimeter(nums))  # Output: 12

# Test Case 3:
nums = [5,5,50] 
print(sol.largestPerimeter(nums))  # Output: -1
