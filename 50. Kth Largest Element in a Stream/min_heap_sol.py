# Kth Largest Element in a Stream
# You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

# You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

# Implement the KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
# int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

# Example 1:

# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Output: [null, 4, 5, 5, 8, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

# Example 2:

# Input:
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

# Output: [null, 7, 7, 7, 8]

# Explanation:

# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8
 

# Constraints:

# 0 <= nums.length <= 104
# 1 <= k <= nums.length + 1
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.


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


