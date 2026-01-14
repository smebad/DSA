# Count Subarrays Where Max Element Appears at Least K Times
# Sliding Window Solution:
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n, max_cnt = max(nums), 0
        l = res = 0

        for r in range(len(nums)):
            if nums[r] == max_n:
                max_cnt += 1
            while max_cnt == k:
                if nums[l] == max_n:
                    max_cnt -= 1
                l += 1
            res += l

        return res

# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once with the right pointer and the left pointer only moves forward.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This sliding window solution is efficient and works well within the given constraints.


# Test Cases
sol = Solution()

# Test Case 1:
nums1 = [1, 3, 2, 3, 3]
k1 = 2
print(sol.countSubarrays(nums1, k1))  # Output: 6

# Test Case 2:
nums2 = [1, 4, 2, 1]
k2 = 3
print(sol.countSubarrays(nums2, k2))  # Output: 0
