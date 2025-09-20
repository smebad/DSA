# Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# Example 2:

# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]
 

# Constraints:

# 1 <= arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# All the elements of arr2 are distinct.
# Each arr2[i] is in arr1.

# Brute Force Solution:
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for num2 in arr2:
            for i, num1 in enumerate(arr1):
                if num1 == num2:
                    res.append(num1)
                    arr1[i] = -1

        arr1.sort()
        for i in range(len(res), len(arr1)):
            res.append(arr1[i])

        return res
    
# Time Complexity: O(m * n + n log n) where m is the length of arr2 and n is the length of arr1. The first for loop takes O(m * n) time, and the second for loop takes O(n log n) time.
# Space Complexity: O(1) if we don't count the output array, otherwise O(n) for the output array.
# This brute force solution is not optimal and can be improved using a counting sort approach.


# Test Cases:
sol = Solution()

# Test Case 1:
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(sol.relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,9,6,7,19]

# Test Case 2:
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(sol.relativeSortArray(arr1, arr2))  # Output: [22,28,8,6,17,44]