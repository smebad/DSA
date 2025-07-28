# Find Lucky Integer in an Array
# Sorting Solution:
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        streak = 0
        for i in range(len(arr) - 1, -1, -1):
            streak += 1
            if i == 0 or (arr[i] != arr[i - 1]):
                if arr[i] == streak:
                    return arr[i]
                streak = 0
        return -1
    
# Time Complexity: O(n log n), where n is the length of the array. This is due to the sorting step.
# Space Complexity: O(1), since we are using a constant amount of space for the streak variable.
# This solution is more efficient than the brute force approach, especially for larger arrays, as it reduces the time complexity significantly.


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