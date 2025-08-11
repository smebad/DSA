# Maximum Ascending Subarray Sum
# Brute Force Solution:
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curSum = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:
                    break
                curSum += nums[j]
            res = max(res, curSum)
        return res
    
# Time Complexity: O(n^2), where n is the length of the input list nums. We use a nested loop to find all ascending subarrays.
# Space Complexity: O(1), we only use a constant amount of extra space for variables.
# This brute force solution is less efficient than the iterative solution but is easier to understand.


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

