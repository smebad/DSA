# Number of Zero-Filled Subarrays
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
# Example 2:

# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
# Example 3:

# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


# Counting consecutive zeros solution:
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                count = 0
            res += count

        return res
    
# Time complexity: O(n), where n is the length of the input array nums. We traverse the array once. In the worst case, the array is completely filled with zeros, so the time complexity is linear.
# Space complexity: O(1), as we use a constant amount of space to store the variables count and res.
# This solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()

# Test Case 1:
nums1 = [1, 3, 0, 0, 2, 0, 0, 4]
print(solution.zeroFilledSubarray(nums1))  # Output: 6

# Test Case 2:
nums2 = [0, 0, 0, 2, 0, 0]
print(solution.zeroFilledSubarray(nums2))  # Output: 9

# Test Case 3:
nums3 = [2, 10, 2019]
print(solution.zeroFilledSubarray(nums3))  # Output: 0