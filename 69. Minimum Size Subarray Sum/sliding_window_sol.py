# Minimum Size Subarray Sum
# Sliding Window Solution:

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res
    
# Time Complexity: O(n) where n is the length of the array. This is because we need to iterate through the array once to find the minimum subarray length.
# Space Complexity: O(1) this is because we are using only a constant amount of space for the pointers l and r.
# This sliding window solution is efficient for large inputs as it has a time complexity of O(n). It is optimal and works well for the problem.


# Test Cases
# Test Case 1:
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums)) # Expected Output: 2

# Test Case 2:
target = 4
nums = [1,4,4]
print(Solution().minSubArrayLen(target, nums)) # Expected Output: 1

# Test Case 3:
target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums)) # Expected Output: 0
