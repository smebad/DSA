# Maximum Ascending Subarray Sum
# Iterative Solution:
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = curSum= nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curSum = 0

            curSum += nums[i]
            res = max(res, curSum)

        return res
    
# Time Complexity: O(n), where n is the length of the input list nums. We iterate through the list once to find the maximum ascending subarray sum.
# Space Complexity: O(1), we only use a constant amount of extra space for variables.
# This iterative solution is efficient and works well within the problem constraints.


# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [10, 20, 30, 5, 10, 50]
print(sol.maxAscendingSum(nums1))  # Output: 65

# Test Case 2:
nums2 = [10, 20, 30, 40, 50]
print(sol.maxAscendingSum(nums2))  # Output: 150

# Test Case 3:
nums3 = [12, 17, 15, 13, 10, 11, 12]
print(sol.maxAscendingSum(nums3))  # Output: 33

