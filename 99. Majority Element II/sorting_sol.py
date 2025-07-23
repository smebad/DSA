# Majority Element II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?


# Sorting solution:
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res, n = [], len(nums)
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            if (j - i) > n // 3:
                res.append(nums[i])
            i = j

        return res
    
# Time Complexity: O(n log n) where n is the length of nums. This is due to the sorting step, which is the most time-consuming operation in this solution.
# Space Complexity: O(1) if we consider the output list as the only additional space used, otherwise O(n) for the input list.
# This solution is not optimal in terms of time complexity compared to the hashmap solution, but it is straightforward and easy to understand.

# Test cases
# Test Case 1:
nums1 = [3, 2, 3]
solution1 = Solution()
print(solution1.majorityElement(nums1))  # Output: [3]

# Test Case 2:
nums2 = [1]
solution2 = Solution()
print(solution2.majorityElement(nums2))  # Output: [1]

# Test Case 3:
nums3 = [1, 2]
solution3 = Solution()
print(solution3.majorityElement(nums3))  # Output: [1, 2]
