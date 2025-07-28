# Find Lucky Integer in an Array
# Brute Force Solution:
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1

        for num in arr:
            cnt = 0
            for a in arr:
                if num == a:
                    cnt += 1
            if cnt == num:
                res = max(res, num)

        return res
    
# Time Complexity: O(n^2), where n is the length of the array. This is because we are iterating through the array twice, once to count the frequency of each number and once to find the lucky number.
# Space Complexity: O(1), since we are using a constant amount of space for the result variable.
# This brute force solution is not optimal for larger arrays, but it works within the given constraints (1 <= arr.length <= 500).

# Test Cases
# Test Case 1:
solution = Solution()
arr = [2, 2, 3, 4]
print(solution.findLucky(arr))  # Output: 2

# Test Case 2:
arr = [1, 2, 2, 3, 3, 3]
print(solution.findLucky(arr))  # Output: 3

# Test Case 3:
arr = [2, 2, 2, 3, 3]
print(solution.findLucky(arr))  # Output: -1