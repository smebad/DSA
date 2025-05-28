# Kth Largest Element in a Stream
# Sorting Solution:

from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
    

# Time Complexity: O(m * n log n) where m is the number of calls to add and n is the size of the array. This is because we sort the array every time we add a new element.
# Space Complexity: O(m) where m is the number of calls to add. O(1) or O(n) if we consider the space used by the input array, but since we are not using any additional data structures, we can consider it O(1) in terms of auxiliary space.
# This solution is less efficient but easier to implement than the min-heap solution, especially for large inputs, as it requires sorting the entire array every time a new element is added.
# However, it is straightforward and works well for small datasets or when the number of elements is manageable.


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


