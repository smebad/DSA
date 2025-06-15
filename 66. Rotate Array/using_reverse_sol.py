# Rotate Array
# Using Reverse Solution:

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# Time Complexity: O(n) where n is the length of the array. This is because we need to iterate through the array once to reverse it.
# Space Complexity: O(1) this is because we are using only a constant amount of space for the pointers l and r.
# This reverse solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.

# Test Cases:
# Test Case 1
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums) # Expected Output: [5,6,7,1,2,3,4]

# Test Case 2
nums = [-1,-100,3,99]
k = 2
Solution().rotate(nums, k)
print(nums) # Expected Output: [3,99,-1,-100]
