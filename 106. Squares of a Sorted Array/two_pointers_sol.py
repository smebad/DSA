# Squares of a Sorted Array
# Two-pointers solution:
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, res = 0, len(nums) - 1, []

        while l <= r:
            if (nums[l] * nums[l]) > (nums[r] * nums[r]):
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        
        return res[::-1]
    
# Time Complexity: O(n) where n is the length of the input array. This is because we traverse the array once using two pointers.
# Space Complexity: O(n) for the output array that stores the squared values. The input array is not modified, and we create a new list to store the results.
# This solution is optimal for the problem constraints, as it leverages the sorted nature of the input array to achieve linear time complexity.


# Test Cases
# Test Case 1:
nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))  # Expected Output: [0, 1, 9, 16, 100]

# Test Case 2:
nums = [-7, -3, 2, 3, 11]
print(Solution().sortedSquares(nums))  # Expected Output: [4, 9, 9, 49, 121]
