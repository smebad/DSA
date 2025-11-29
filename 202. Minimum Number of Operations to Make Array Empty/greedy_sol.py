# Minimum Number of Operations to Make Array Empty
# Greedy Solution:
from collections import Counter
from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num, cnt in count.items():
            if cnt == 1:
                return -1
            res += math.ceil(cnt / 3)

        return res
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once to count frequencies.
# Space Complexity: O(k), where k is the number of unique elements in nums. This space is used by the frequency counter.
# This greedy approach efficiently calculates the minimum operations by maximizing the use of three-element deletions.


# Test Cases
solution = Solution()

# Test Case 1:
nums1 = [2,3,3,2,2,4,2,3,4]
print(solution.minOperations(nums1))  # Expected output: 4

# Test Case 2:
nums2 = [2,1,2,2,3,3]
print(solution.minOperations(nums2))  # Expected output: -1
