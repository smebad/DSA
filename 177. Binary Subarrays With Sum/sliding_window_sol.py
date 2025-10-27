# Binary Subarrays With Sum
# Sliding Window Solution:
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            res = l = cur = 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur > x:
                    cur -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res

        return helper(goal) - helper(goal - 1)
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array twice (once for each call to helper), and each traversal takes linear time.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This sliding window approach is efficient for counting the number of subarrays with a given sum in a binary array.


# Test Cases:
# Test Case 1:
nums1 = [1, 0, 1, 0, 1]
goal1 = 2
print(Solution().numSubarraysWithSum(nums1, goal1))  # Output: 4

# Test Case 2:
nums2 = [0, 0, 0, 0, 0]
goal2 = 0
print(Solution().numSubarraysWithSum(nums2, goal2))  # Output: 15
