# K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104


# Sorting solution:
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res
    
# Time Complexity: O(k * log n) where n is the number of points. This is because we are using a min-heap to extract the k closest points, and each extraction takes O(log n) time. This time complexity is efficient given the constraints (1 <= k <= points.length <= 10^4).
# Space Complexity: O(n) for storing the points in the min-heap. This is necessary to keep track of all points and their distances from the origin.
# However, this and the sorting solution both have a time complexity of O(n log n) due to the sorting step, but the heap solution is more efficient for extracting k closest points.


# Test Cases:
# Test Case 1:
points = [[1,3],[-2,2]]
k = 1
print(Solution().kClosest(points, k))  # Output: [[-2,2]]

# Test Case 2:
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points, k))  # Output: [[3,3],[-2,4]]