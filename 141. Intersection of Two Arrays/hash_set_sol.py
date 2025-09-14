# Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Hash-set Solution:
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)

        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res

# Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 respectively. This is because we are iterating over both arrays once each.
# Space Complexity: O(n) where n is the length of the seen set in the worst case when all elements of nums1 are unique.
# This solution is optimal for the given problem constraints.


# Test Cases:
sol = Solution()

# Test Case 1:
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1, nums2))  # Expected Output: [2]

# Test Case 2:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersection(nums1, nums2))  # Expected Output: [9, 4]