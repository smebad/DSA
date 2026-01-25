# Move Zeroes
# Two Pointers Solution:
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

# Time complexity: O(n) where n is the length of the input array. This is because we traverse the array once.
# Space complexity: O(1) since we are modifying the array in place without using any additional data structures.
# This solution uses two pointers: one to track the position of the last non-zero element (`l`) and another to iterate through the array (`r`). When a non-zero element is found, it is swapped with the element at the `l` pointer, and `l` is incremented. This ensures that all non-zero elements are moved to the front while maintaining their order. So this two pointers approach is efficient and meets the problem's requirements.

# Test cases
# Test Case 1:
sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Test Case 2:
nums = [0]
sol.moveZeroes(nums)
print(nums)  # Output: [0]
