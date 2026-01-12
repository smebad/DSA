# Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


# Sliding Window Solution:
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = res = 0
        for r in range(len(nums)):
            k -= (1 if nums[r] == 0 else 0)
            while k < 0:
                k += (1 if nums[l] == 0 else 0)
                l += 1
            res = max(res, r - l + 1)
        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once with the right pointer, and the left pointer only moves forward.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This sliding window approach is efficient because it efficiently finds the longest subarray with at most k zeros by dynamically adjusting the window size based on the number of zeros encountered.


# Test Cases:
solution = Solution()

# Test Case 1:
nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
print(solution.longestOnes(nums1, k1))  # Output: 6

# Test Case 2:
nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3
print(solution.longestOnes(nums2, k2))  # Output: 10

# Test Case 3:
nums3 = [1,0,1,0,1]
k3 = 1
print(solution.longestOnes(nums3, k3))  # Output: 4