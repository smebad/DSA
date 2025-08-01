# Find Minimum in Rotated Sorted Array
# Binary search Solution:

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
    
# Time Complexity: O(log n) because we are using binary search to find the minimum element in the rotated sorted array. In each iteration, we reduce the search space by half, leading to logarithmic time complexity.
# Space Complexity: O(1) because we are using a constant amount of space for variables and not using any additional data structures that grow with the input size.
# The binary search solution efficiently finds the minimum element in a rotated sorted array by leveraging the properties of the array's rotation. It maintains a pointer to the left and right ends of the array and narrows down the search space based on the mid-point value compared to the left and right pointers.
# This approach meets the requirement of O(log n) time complexity and O(1) space complexity.

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
