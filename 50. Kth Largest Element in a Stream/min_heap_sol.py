# Kth Largest Element in a Stream
# Min-Heap Solution:

import heapq
from typing import List

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    

# Time Complexity: O(m * log k) for m calls to add, where k is the size of the min-heap. This is because each add operation involves a push and possibly a pop operation on the heap, both of which take O(log k) time. Logarithmic time is due to the properties of heaps.
# Space Complexity: O(k) for storing the k largest elements in the min-heap. The heap will never grow larger than k elements, so the space used is proportional to k.
# Note: The min-heap is used to efficiently keep track of the k largest elements. The smallest element in the heap will be the kth largest element in the stream.
# This solution is efficient for maintaining the kth largest element in a dynamic stream of scores, allowing for quick updates and retrievals as new scores are added.


# Test Cases:
if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # Output: 4
    print(kthLargest.add(5))  # Output: 5
    print(kthLargest.add(10)) # Output: 5
    print(kthLargest.add(9))  # Output: 8
    print(kthLargest.add(4))  # Output: 8

    kthLargest2 = KthLargest(4, [7, 7, 7, 7, 8, 3])
    print(kthLargest2.add(2))  # Output: 7
    print(kthLargest2.add(10)) # Output: 7
    print(kthLargest2.add(9))  # Output: 7
    print(kthLargest2.add(9))  # Output: 8


