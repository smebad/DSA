# Merge Sorted Array
# Sorting solution:

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

# Time Complexity: O((m + n) log(m + n)) where m and n are the lengths of the two arrays. This is because we are sorting the merged array.
# Space Complexity: O(1) or O(m + n) if we count the space used by the sorted array. No additional data structures are used.

# Test Cases:
# Test Case 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Expected Output: [1, 2, 2, 3, 5, 6]

# Test Case 2:
nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Expected Output: [1]

# Test Case 3:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Expected Output: [1]

