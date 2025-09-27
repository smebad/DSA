# Minimum Difference Between Highest and Lowest of K Scores
# Sorting + Sliding Window Solution:
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res
    
# Time Complexity: O(n log n), where n is the number of elements in the array. This is due to the sorting step. The sliding window traversal takes O(n) time, but the overall time complexity is dominated by the sorting operation.
# Space Complexity: O(1) if we ignore the space used for sorting (which is typically O(log n) for the sorting algorithm). The sliding window approach uses a constant amount of extra space.
# This solution is efficient and leverages sorting followed by a sliding window technique to find the minimum difference between the highest and lowest scores among any k students.


# Test cases:
sol = Solution()

# Test Case 1:
nums1 = [90]
k1 = 1
print(sol.minimumDifference(nums1, k1))  # Output: 0

# Test Case 2:
nums2 = [9,4,1,7]
k2 = 2
print(sol.minimumDifference(nums2, k2))  # Output: 2
