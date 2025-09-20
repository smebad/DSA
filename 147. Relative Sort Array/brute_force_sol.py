# Relative Sort Array
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
