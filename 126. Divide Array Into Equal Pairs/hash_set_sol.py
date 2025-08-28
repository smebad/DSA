# Divide Array Into Equal Pairs
# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

 

# Example 1:

# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation: 
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: 
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
 

# Constraints:

# nums.length == 2 * n
# 1 <= n <= 500
# 1 <= nums[i] <= 500


# Hash-Set Solution:
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()

        for num in nums:
            if num not in odd_set:
                odd_set.add(num)
            else:
                odd_set.remove(num)

        return not len(odd_set)

# Time Complexity: O(n), where n is the length of the input array. In this solution, we traverse the array once to build the set and then again to check the counts, resulting in a linear time complexity.
# Space Complexity: O(n), where n is the number of unique elements in the input array. In the worst case, we may store all elements in the set.
# This approach is efficient and works well within the given constraints.


# Test Cases
sol = Solution()
# Test Case 1:
nums1 = [3,2,3,2,2,2]
print(sol.divideArray(nums1))  # Output: True

# Test Case 2:
nums2 = [1,2,3,4]
print(sol.divideArray(nums2))  # Output: False