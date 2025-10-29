# Length of Longest Subarray With at Most K Frequency
# Sliding Window Solution:
from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
# Time Complexity: O(n), where n is the length of the input array nums. Each element is processed at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(n), in the worst case, we may need to store the frequency of all elements in the count dictionary.
# This sliding window solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1
print(sol.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))  # Expected output: 6

# Test Case 2
print(sol.maxSubarrayLength([1,2,1,2,1,2,1,2], 1))  # Expected output: 2

# Test Case 3
print(sol.maxSubarrayLength([5,5,5,5,5,5,5], 4))  # Expected output: 4
