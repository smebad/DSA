# Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
 

# Constraints:

# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length


# Three Pointers Solution:
from typing import List
class Solution: 
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd = 0, 0
        l, m = 0, 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1

            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l

            if odd == k:
                while not nums[m] % 2:
                    m += 1
                res += (m - l) + 1

        return res
    
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once with the right pointer and adjust the left pointer as needed.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This solution efficiently counts the number of nice subarrays using a three-pointer technique, maintaining the count of odd numbers and adjusting the left pointer to ensure we only consider valid subarrays.

# Test Cases
# Test Case 1:
nums = [1, 1, 2, 1, 1]
k = 3
# Expected Output: 2
print(Solution().numberOfSubarrays(nums, k))

# Test Case 2:
nums = [2, 4, 6]
k = 1
# Expected Output: 0
print(Solution().numberOfSubarrays(nums, k))
