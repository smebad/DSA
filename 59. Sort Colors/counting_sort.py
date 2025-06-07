# Sort Colors
# Counting Sort Solution:

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

# Time Complexity: O(n) where n is the length of nums array. This is because we iterate through the array once to count the frequency of each color, and then we iterate through the array again to place the colors in the correct order.
# Space Complexity: O(1) since we only use a constant amount of extra space to store the count array.
# Thiscounting sort solution is a good solution for small inputs as it takes O(n) time complexity.


# Test Cases:
# Test Case 1
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums) # Output: [0,0,1,1,2,2]

# Test Case 2
nums = [2,0,1]
Solution().sortColors(nums)
print(nums) # Output: [0,1,2]
