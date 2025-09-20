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

# Hashmap Solution:
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        res = []
        for num in arr2:
            res += [num] * count.pop(num)

        for num in sorted(count):
            res += [num] * count[num]

        return res
    
# Time Complexity: O(n + m + n log n) where n is the length of arr1 and m is the length of arr2. In this solution, we first count the occurrences of each number in arr1 which takes O(n) time. Then we iterate through arr2 which takes O(m) time. Finally, we sort the remaining elements in count which takes O(k log k) time where k is the number of unique elements not in arr2. In the worst case, k can be equal to n, leading to O(n log n) time complexity.
# Space Complexity: O(n) for the count dictionary and the output array.
# This hashmap solution is more efficient than the brute force solution and is optimal for this problem.


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