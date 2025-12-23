# Maximum Distance in Arrays
# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

# Return the maximum distance.

 

# Example 1:

# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Example 2:

# Input: arrays = [[1],[1]]
# Output: 0
 

# Constraints:

# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.


# Solution:
from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(
                res,
                arr[-1] - cur_min,
                cur_max - arr[0]
            )
            
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        return res

# Time Complexity: O(m), where m is the number of arrays.
# Space Complexity: O(1)
# This solution is efficient and works well within the given constraints.


# Test Cases:
solution = Solution()

# Test Case 1
arrays1 = [[1,2,3],[4,5],[1,2,3]]
print(solution.maxDistance(arrays1))  # Expected output: 4

# Test Case 2
arrays2 = [[1],[1]]
print(solution.maxDistance(arrays2))  # Expected output: 0
