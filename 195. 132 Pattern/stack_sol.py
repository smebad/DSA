# 132 Pattern
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

# Constraints:

# n == nums.length
# 1 <= n <= 2 * 105
# -109 <= nums[i] <= 109
 

# Stack Solution:
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curMin = nums[0]

        for i in range(1, len(nums)):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            if stack and nums[i] > stack[-1][1]:
                return True

            stack.append([nums[i], curMin])
            curMin = min(curMin, nums[i])

        return False

# Time Complexity: O(n), where n is the length of the input array nums. Each element is pushed and popped from the stack at most once.
# Space Complexity: O(n) in the worst case, where all elements are stored in the stack.
# This stack solution is efficient and effectively checks for the 132 pattern by maintaining a stack of potential candidates while iterating through the array.


# Test Cases
# Test Case 1:
nums1 = [1, 2, 3, 4]
print(Solution().find132pattern(nums1))  # Expected Output: False

# Test Case 2:
nums2 = [3, 1, 4, 2]
print(Solution().find132pattern(nums2))  # Expected Output: True

# Test Case 3:
nums3 = [-1, 3, 2, 0]
print(Solution().find132pattern(nums3))  # Expected Output: True