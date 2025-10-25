# Frequency of the Most Frequent Element
# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:

# Input: nums = [3,9,6], k = 2
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= 105


# Sliding Window Solution:
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = res = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)

        return res
    
# Time Complexity: O(n log n), where n is the length of the input array nums. This is due to the sorting step. The sliding window traversal takes O(n) time.
# Space Complexity: O(1) or O(n) depending on the sorting algorithm used. If an in-place sorting algorithm is used, the space complexity is O(1). Otherwise, it may require O(n) space.
# This sliding window approach is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1
nums1 = [1,2,4]
k1 = 5
print(sol.maxFrequency(nums1, k1))  # Expected Output: 3

# Test Case 2
nums2 = [1,4,8,13]
k2 = 5
print(sol.maxFrequency(nums2, k2))  # Expected Output: 2

# Test Case 3
nums3 = [3,9,6]
k3 = 2
print(sol.maxFrequency(nums3, k3))  # Expected Output: 1