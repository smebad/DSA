# Minimum Operations to Reduce X to Zero
# Sliding Window Solution:
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        cur_sum = 0
        max_window = -1
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_window = max(max_window, r - l + 1)

        return -1 if max_window == -1 else len(nums) - max_window

# Time Complexity: O(n), where n is the length of the nums array. We traverse the array once using a sliding window approach.
# Space Complexity: O(1), as we use only a constant amount of extra space.
# This sliding window solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()
nums1 = [1, 1, 4, 2, 3]
x1 = 5
print(solution.minOperations(nums1, x1))  # Output: 2

nums2 = [5, 6, 7, 8, 9]
x2 = 4
print(solution.minOperations(nums2, x2))  # Output: -1

nums3 = [3, 2, 20, 1, 1, 3]
x3 = 10
print(solution.minOperations(nums3, x3))  # Output: 5
