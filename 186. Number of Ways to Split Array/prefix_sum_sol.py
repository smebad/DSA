# Number of Ways to Split Array
# Prefix Sum Solution:
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = res = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            res += 1 if left >= right else 0

        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to compute the total sum and once more to count valid splits.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This prefix sum solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()

# Test Case 1:
nums1 = [10, 4, -8, 7]
print(solution.waysToSplitArray(nums1))  # Output: 2

# Test Case 2:
nums2 = [2, 3, 1, 0]
print(solution.waysToSplitArray(nums2))  # Output: 2
