# Minimum Difference Between Highest and Lowest of K Scores
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

 

# Example 1:

# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Example 2:

# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.
 

# Constraints:

# 1 <= k <= nums.length <= 1000
# 0 <= nums[i] <= 105


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