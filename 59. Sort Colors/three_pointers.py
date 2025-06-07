# Sort Colors
# Three pointers Solution:

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

# Time Complexity: O(n) where n is the length of nums array. This is because we iterate through the array once to count the frequency of each color, and then we iterate through the array again to place the colors in the correct order.
# Space Complexity: O(1) since we only use a constant amount of extra space to store the count array.
# This three pointers solution is a good solution for small inputs as it takes O(n) time complexity.


# Test Cases:
# Test Case 1
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums) # Output: [0,0,1,1,2,2]

# Test Case 2
nums = [2,0,1]
Solution().sortColors(nums)
print(nums) # Output: [0,1,2]
