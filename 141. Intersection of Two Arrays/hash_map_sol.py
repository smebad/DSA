# Intersection of Two Arrays
# Hash-map Solution:
from typing import List
from collections import defaultdict

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(int)
        for num in nums1:
            seen[num] = 1

        res = []
        for num in nums2:
            if seen[num] == 1:
                seen[num] = 0
                res.append(num)
        return res

# Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 respectively. This is because we are iterating over both arrays once each.
# Space Complexity: O(n) where n is the length of the seen dictionary in the worst case when all elements of nums1 are unique.
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
