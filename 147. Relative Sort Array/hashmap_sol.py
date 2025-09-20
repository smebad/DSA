# Relative Sort Array
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
