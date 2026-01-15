# Maximum Beauty of an Array After Applying Operation
# Sliding Window Solution:
from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1

            res = max(res, r - l + 1)

        return res

# Time Complexity: O(n log n) where n is the length of nums due to sorting. The sliding window traversal takes O(n) time.
# Space Complexity: O(1) as we are using only a constant amount of extra space.
# This sliding window solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()
nums1 = [4, 6, 1, 2]
k1 = 2
print(solution.maximumBeauty(nums1, k1))  # Output: 3

nums2 = [1, 1, 1, 1]
k2 = 10
print(solution.maximumBeauty(nums2, k2))  # Output: 4
