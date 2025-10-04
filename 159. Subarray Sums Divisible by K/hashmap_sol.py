# Subarray Sums Divisible by K
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104

# Prefix + Hashmap Solution:
from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            res += prefix_cnt[remain]
            prefix_cnt[remain] += 1

        return res
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to compute the prefix sums and their remainders.
# Space Complexity: O(k), where k is the divisor. In the worst case, we may store up to k different remainders in the hashmap.
# This hashmap + prefix sum approach efficiently counts the number of subarrays whose sums are divisible by k.


# Test Cases:
# Test Case 1:
nums = [4, 5, 0, -2, -3, 1]
k = 5
print(Solution().subarraysDivByK(nums, k))  # Output: 7

# Test Case 2:
nums = [5]
k = 9
print(Solution().subarraysDivByK(nums, k))  # Output: 0