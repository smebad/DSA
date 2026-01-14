# Count Subarrays Where Max Element Appears at Least K Times
# You are given an integer array nums and a positive integer k.

# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

# A subarray is a contiguous sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
# Example 2:

# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105


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
