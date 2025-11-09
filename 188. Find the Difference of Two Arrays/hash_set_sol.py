# Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
# Example 2:

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000


# Hash Set Solution:
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set, num2Set = set(nums1), set(nums2)
        res1, res2 = [], []

        for num in num1Set:
            if num not in num2Set:
                res1.append(num)

        for num in num2Set:
            if num not in num1Set:
                res2.append(num)

        return [res1, res2]
    
# Time Complexity: O(n + m), where n and m are the lengths of nums1 and nums2 respectively. This is because we are creating sets from both arrays and then iterating through each set once.
# Space Complexity: O(n + m) in the worst case, where all elements in nums1 and nums2 are distinct. This is due to the space used by the sets num1Set and num2Set.
# This hash set solution is efficient in both time and space.


# Test Cases
# Test Case 1:
nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[1,3],[4,6]]

# Test Case 2:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[3],[]]

# Test Case 3:
nums1 = [4,5,6]
nums2 = [1,2,3]
print(Solution().findDifference(nums1, nums2)) # Expected Output: [[4,5,6],[1,2,3]]