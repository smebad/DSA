# Intersection of Two Arrays
# Brute Force Solution:
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    res.add(i)
                    break
        return list(res)
    
# Time Complexity: O(n*m) where n and m are the lengths of nums1 and nums2 respectively. This is because we are iterating over the two arrays once each.
# Space Complexity: O(n) where n is the length of the result set in the worst case when all elements are common.
# This solution is not optimal for large input sizes due to its quadratic time complexity.


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
