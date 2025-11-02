# Continuous Subarray Sum
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false


# Prefix Sum + Hashmap Solution:
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}  # remainder -> end index
        total = 0

        for i, num in enumerate(nums):
            total += num
            if k != 0:
                r = total % k
            else:
                r = total

            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return False
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(k), where k is the number of possible remainders (0 to k-1). In the worst case, we may store up to k different remainders in the hashmap.
# This prefix + hashmap solution is efficient and works well within the given constraints.


# Test Cases:
# Test Case 1:
nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))  # Output: True

# Test Case 2:
nums = [23, 2, 6, 4, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))  # Output: True

# Test Case 3:
nums = [23, 2, 6, 4, 7]
k = 13
print(Solution().checkSubarraySum(nums, k))  # Output: False
