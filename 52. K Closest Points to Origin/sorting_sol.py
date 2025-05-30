# K Closest Points to Origin
# Sorting solution:

from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
    
# Time Complexity: O(n log n) where n is the number of points. This is because we sort the points based on their distance from the origin. 
# Space Complexity: O(1) or O(n) depending on the sorting algorithm used. In Python, the built-in sort function uses Timsort which has a space complexity of O(n) in the worst case.
# This solution is efficient and works well within the constraints given (1 <= k <= points.length <= 10^4).


# Test Cases:
# Test Case 1:
points = [[1,3],[-2,2]]
k = 1
print(Solution().kClosest(points, k))  # Output: [[-2,2]]

# Test Case 2:
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points, k))  # Output: [[3,3],[-2,4]]
