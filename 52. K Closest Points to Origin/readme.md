# K Closest Points to Origin - LeetCode

## Problem Statement

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance is measured using the Euclidean distance:
$\text{distance} = \sqrt{(x^2 + y^2)}$
Since we only care about comparing distances, we can ignore the square root (as it's a monotonic function).

You may return the answer in any order. The answer is guaranteed to be unique except for the order.

### Example 1:

```python
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: sqrt(8) < sqrt(10), so (-2,2) is closer to origin.
```

### Example 2:

```python
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

---

## Sorting-Based Solution

```python
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort points based on their distance from the origin (0,0)
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # Return the first k points from the sorted list
        return points[:k]
```

### Explanation:

* We calculate the squared distance for each point: `x^2 + y^2`.
* Sort the points in ascending order based on this squared distance.
* Return the first `k` points.

### Time & Space Complexity:

* **Time Complexity**: O(n log n) due to the sort operation.
* **Space Complexity**: O(1) extra space (in-place sorting), or O(n) depending on the sorting algorithm (Timsort in Python).

---

## Min-Heap-Based Solution

```python
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)  # Squared Euclidean distance
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)  # Transform the list into a min-heap based on distances

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Extract the point with the smallest distance
            res.append([x, y])
            k -= 1

        return res
```

### Explanation:

* We first compute the squared distance for each point and store `[distance, x, y]` in a list.
* Use `heapq.heapify()` to build a min-heap from this list.
* Extract the smallest `k` elements (closest points).

### Time & Space Complexity:

* **Time Complexity**: O(n + k log n)

  * Heapify takes O(n)
  * Popping `k` elements takes O(k log n)
* **Space Complexity**: O(n) to store all points in the heap.

---

## Comparing the Two Solutions

| Feature                  | Sorting-Based Solution | Heap-Based Solution |
| ------------------------ | ---------------------- | ------------------- |
| Time Complexity          | O(n log n)             | O(n + k log n)      |
| Space Complexity         | O(1) or O(n)           | O(n)                |
| Efficiency for Large `k` | Efficient              | Efficient           |
| Efficiency for Small `k` | Less efficient         | More efficient      |

---

## Which Solution is Better and Why?

* The **heap-based solution** is more optimal, especially when `k` is much smaller than `n`.
* It avoids sorting the entire list, instead focusing only on the top `k` closest points.
* Therefore, it is generally preferred for performance in large datasets.

---

## Conclusion

Both solutions solve the problem correctly and efficiently under given constraints.
For smaller values of `k` or performance-critical applications, the heap-based method is recommended due to its better average runtime and lower unnecessary sorting overhead.
