# K Closest Points to Origin
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
