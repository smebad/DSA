# Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106


# Sliding Window Solution:
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            res += (r - l + 1)
        return res
    
# Time Complexity: O(n), where n is the length of the input array nums. Each element is processed at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This sliding window approach is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()

# Test Case 1
nums1 = [10, 5, 2, 6]
k1 = 100
print(solution.numSubarrayProductLessThanK(nums1, k1))  # Output: 8

# Test Case 2
nums2 = [1, 2, 3]
k2 = 0
print(solution.numSubarrayProductLessThanK(nums2, k2))  # Output: 0