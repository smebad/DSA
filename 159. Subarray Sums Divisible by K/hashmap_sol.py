# Subarray Sums Divisible by K
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
