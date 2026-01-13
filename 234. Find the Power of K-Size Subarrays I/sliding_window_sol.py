# Find the Power of K-Size Subarrays I
# You are given an array of integers nums of length n and a positive integer k.

# The power of an array is defined as:

# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all subarrays of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

# Example 1:

# Input: nums = [1,2,3,4,3,2,5], k = 3

# Output: [3,4,-1,-1,-1]

# Explanation:

# There are 5 subarrays of nums of size 3:

# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.
# Example 2:

# Input: nums = [2,2,2,2,2], k = 4

# Output: [-1,-1]

# Example 3:

# Input: nums = [3,2,3,2,3,2], k = 2

# Output: [-1,3,-1,3,-1]

 

# Constraints:

# 1 <= n == nums.length <= 500
# 1 <= nums[i] <= 105
# 1 <= k <= n


# Sliding Window Solution:
from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        consec_count = 1

        for r in range(len(nums)):
            if r > 0 and nums[r - 1] == nums[r]:
                consec_count += 1

            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    consec_count -= 1
                l += 1

            if r - l + 1 == k:
                res.append(max(nums[l:r + 1]) if consec_count == k - 1 else -1)
        return res
    
# Time Complexity: O(n * k) where n is the length of nums and k is the size of the subarray.
# Space Complexity: O(1) as we are using only constant extra space.
# # This sliding window approach efficiently checks each subarray of size k for the required conditions and computes the result accordingly.


# Test Cases:
sol = Solution()

# Test Case 1
nums = [1,2,3,4,3,2,5]
k = 3
print(sol.resultsArray(nums, k))

# Test Case 2 
nums = [2,2,2,2,2]
k = 4
print(sol.resultsArray(nums, k))

# Test Case 3
nums = [3,2,3,2,3,2]
k = 2
print(sol.resultsArray(nums, k))
                    