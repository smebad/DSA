# Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# Math Solution:
from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for num, c in count.items():
            res += c * (c - 1) // 2
        return res

# Time Complexity: O(n), where n is the length of the input array. In this case, we are using a mathematical approach to count the pairs.
# Space Complexity: O(n), where n is the number of unique elements in the input array.
# This solution is more efficient than the brute force approach, especially for larger input sizes.

# Test Cases
sol = Solution()

# Test Case 1:
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums))  # Output: 4

# Test Case 2:
nums = [1,1,1,1]
print(sol.numIdenticalPairs(nums))  # Output: 6

# Test Case 3:
nums = [1,2,3]
print(sol.numIdenticalPairs(nums))  # Output: 0
