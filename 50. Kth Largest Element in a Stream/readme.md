# Kth Largest Element in a Stream - LeetCode

## Problem Description

Imagine you're working in a university admissions office, and students are continuously submitting their test scores. Your task is to **dynamically maintain the kth highest test score** from a stream of incoming scores. This helps in setting real-time cut-off marks for interviews and admissions.

The problem is to design a class `KthLargest` with two primary operations:

* `KthLargest(int k, int[] nums)`: Initializes the object with an integer `k` and a stream of scores `nums`.
* `int add(int val)`: Adds a new test score `val` to the stream and returns the **kth largest** element among all elements seen so far.

---

## Intuition: What Is the "Kth Largest" in a Stream?

If you had a list of scores like `[10, 7, 5, 3]` and were asked for the 2nd largest, the answer would be `7`. As more scores come in, this value can change.

To keep finding the **kth largest** quickly as new elements are added, we need a data structure that helps us do this efficiently.

---

## Min-Heap Solution (Efficient and Optimal)

```python
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)  # Convert the list to a valid min-heap
        # Keep only the k largest elements in the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Add the new score
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # Remove smallest if heap exceeds size k
        return self.minHeap[0]  # The root of the heap is the kth largest
```

### How It Works

* A **min-heap** of size `k` keeps track of the top `k` elements.
* The **smallest element in the heap is the kth largest overall**, because the heap only holds the top `k` elements.
* On each `add(val)`, we insert the value and remove the smallest if we exceed `k`.

### Time and Space Complexity

* **Time Complexity:** `O(log k)` per `add` operation
* **Total Time for m adds:** `O(m * log k)`
* **Space Complexity:** `O(k)`
* **Why Optimal?** Heaps allow maintaining the top `k` elements efficiently without sorting the whole list every time.

---

## Sorting-Based Solution (Naive and Less Efficient)

```python
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)     # Add the new value to the list
        self.arr.sort()          # Sort the list
        return self.arr[-self.k] # Return the kth largest
```

### How It Works

* Adds new element to the list and sorts it.
* Returns the element at position `len - k`.

### Time and Space Complexity

* **Time Complexity:** `O(n log n)` for each `add` (due to sorting)
* **Total Time for m adds:** `O(m * n log n)`
* **Space Complexity:** `O(n)` (we store the full list)
* **Why Less Efficient?** Sorting the entire array every time is costly for large inputs.

---

## Comparison of Solutions

| Aspect       | Min-Heap Solution            | Sorting Solution         |
| ------------ | ---------------------------- | ------------------------ |
| Efficiency   | Fast and optimal             | Slower                   |
| Space Usage  | Small (`O(k)`)               | Larger (`O(n)`)          |
| Suitable For | Large, dynamic data streams  | Small datasets           |
| Logic        | Maintain top `k` with a heap | Sort full list each time |

---

## Conclusion

* Use the **min-heap solution** for real-world, performance-critical applications.
* The **sorting solution** can help understand the basics or be used for small inputs.
* Always remember that **`heapq` in Python is a min-heap**, and we use it to keep the smallest of the top `k` elements at the top.

The heap-based approach is optimal in both time and space when dealing with dynamic streams where frequent updates and queries are expected.
