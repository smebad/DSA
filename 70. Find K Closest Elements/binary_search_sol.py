# Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104


# Binary Search Solution:
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]
    
# Time Complexity: O(log(n-k)) where n is the length of the array and k is the number of closest elements to find. We got log (n-k) because we are performing a binary search on the range of indices where the k closest elements can start.
# Space Complexity: O(k) for the output list that contains the k closest elements.
# Note: The binary search is used to find the starting index of the k closest elements in the sorted array. The condition checks whether the left or right side of the middle element is closer to x, and adjusts the search range accordingly.
# This solution efficiently narrows down the range of indices to find the k closest elements to x in the sorted array.

# Test Cases
# Test Case 1:
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(Solution().findClosestElements(arr, k, x))  # Output: [1, 2, 3, 4]

# Test Case 2:
arr = [1, 1, 2, 3, 4, 5]
k = 4
x = -1
print(Solution().findClosestElements(arr, k, x))  # Output: [1, 1, 2, 3]
