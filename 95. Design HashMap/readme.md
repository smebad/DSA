# Design HashMap - LeetCode - LeetCode

## Problem Summary

The goal of this problem is to implement a custom HashMap from scratch without using any built-in hash table libraries. A HashMap is a data structure that allows storing key-value pairs with efficient operations like insert, get, and delete. You are required to create a class `MyHashMap` that supports the following methods:

* `put(key, value)`: Insert or update a (key, value) pair.
* `get(key)`: Retrieve the value for a given key. Return -1 if not found.
* `remove(key)`: Remove the key and its associated value.

### Constraints

* `0 <= key, value <= 10^6`
* At most `10^4` operations

---

## Solution 1: Array-Based Implementation

This solution uses a fixed-size array to store values directly at the index corresponding to the key.

### Code with Comments

```python
class MyHashMap:
    def __init__(self):
        # Create an array of size 1000001 initialized with -1
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Directly place value at index 'key'
        self.map[key] = value

    def get(self, key: int) -> int:
        # Return the value at index 'key'; -1 if not set
        return self.map[key]

    def remove(self, key: int) -> None:
        # Reset the index to -1 to simulate deletion
        self.map[key] = -1
```

### Approach and Logic

* Keys are directly used as indexes.
* This makes every operation O(1) since we directly access the array.
* It only works because the key range is known and limited (0 to 10^6).

### Time and Space Complexity

* **Time Complexity**: O(1) for `put`, `get`, and `remove`
* **Space Complexity**: O(n) = O(10^6) to store all possible keys

### Pros and Cons

* **Pros**: Extremely fast operations
* **Cons**: Wastes a lot of memory if few keys are used

---

## Solution 2: Linked List (Chaining) Implementation

This method uses hashing with separate chaining to handle collisions. Each bucket contains a linked list.

### Code with Comments

```python
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        # Create 1000 buckets each with a dummy head node
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key: int) -> int:
        # Simple hash function using modulo
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                # Update value if key already exists
                cur.next.val = value
                return
            cur = cur.next
        # If key not found, add new node
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
```

### Approach and Logic

* The array size is much smaller (1000 buckets).
* Each index is a linked list to handle collisions.
* When two keys hash to the same index, they’re chained in a list.

### Time and Space Complexity

* **Time Complexity**: O(n/k) per operation in the worst case

  * `n`: number of elements in the map
  * `k`: number of buckets (1000)
* **Space Complexity**: O(k + m)

  * `k`: number of buckets
  * `m`: number of elements (linked list nodes)

### Pros and Cons

* **Pros**: More memory-efficient when keys are sparse
* **Cons**: Slightly slower than array-based due to list traversal

---

## Conclusion: Which Solution is Best?

* If memory is not a concern and you want the fastest operations: **Array-based** is better.
* If memory usage is critical or keys are sparse: **Linked List with Chaining** is more optimal.

In competitive programming where key ranges are known and space is allowed, array-based is preferred. In real-world applications with unknown key ranges, linked list chaining is safer and more scalable.
