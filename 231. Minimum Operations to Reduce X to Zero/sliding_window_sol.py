# Minimum Operations to Reduce X to Zero
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109


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