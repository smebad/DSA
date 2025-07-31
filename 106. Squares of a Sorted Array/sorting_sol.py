# Squares of a Sorted Array
# Sorting solution:
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
    
# Time Complexity: O(n log n) due to sorting operation where n is the length of the input array. This is because sorting takes O(n log n) time in the worst case.
# Space Complexity: O(1) if we consider the input array as the output array, otherwise O(n) for storing the squared values in a new array.
# This solution is straightforward but not optimal for the problem constraints, as it does not utilize the fact that the input array is already sorted.


# Test Cases
# Test Case 1:
nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))  # Expected Output: [0, 1, 9, 16, 100]

# Test Case 2:
nums = [-7, -3, 2, 3, 11]
print(Solution().sortedSquares(nums))  # Expected Output: [4, 9, 9, 49, 121]
