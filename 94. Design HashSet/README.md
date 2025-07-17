# Design HashSet - LeetCode

## Problem Explanation

The "Design HashSet" problem asks us to implement a basic version of a set data structure. Unlike a typical set in Python, we cannot use built-in hash table libraries. Instead, we must implement the three core operations ourselves:

* `add(key)`: Insert a value into the set.
* `remove(key)`: Remove a value from the set.
* `contains(key)`: Check if a value exists in the set.

### Constraints

* Keys range from `0` to `10^6`.
* Up to `10^4` operations will be performed.

---

## Solution 1: Brute Force Using a List

This is the most straightforward approach where we use a Python list to store the elements.

```python
class MyHashSet:

    def __init__(self):
        self.data = []  # List to store elements

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)  # Add only if it's not already present

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)  # Remove the key if it exists

    def contains(self, key: int) -> bool:
        return key in self.data  # Check if the key exists in the list
```

### Time and Space Complexity

* **Time:** O(n) for `add`, `remove`, and `contains`, where n is the number of elements in the list.
* **Space:** O(n) for the list that stores elements.

### Analysis

This approach is simple but inefficient for large data because list operations like `in` and `remove` are O(n).

---

## Solution 2: Boolean Array

This approach uses a fixed-size boolean array to track the presence of elements.

```python
class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001  # Initialize a boolean array with all False

    def add(self, key: int) -> None:
        self.data[key] = True  # Mark the index as True

    def remove(self, key: int) -> None:
        self.data[key] = False  # Set the index back to False

    def contains(self, key: int) -> bool:
        return self.data[key]  # Return the value at that index
```

### Time and Space Complexity

* **Time:** O(1) for `add`, `remove`, and `contains`.
* **Space:** O(10^6) for the boolean array.

### Analysis

Very efficient in time, but uses a lot of memory. Suitable only when the key range is small and fixed.

---

## Solution 3: Linked List with Hashing (Chaining)

This method uses hashing and handles collisions using a linked list.

```python
class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10000)]  # Initialize buckets

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]  # Choose the bucket based on hash
        while cur.next:
            if cur.next.key == key:
                return  # Key already exists
            cur = cur.next
        cur.next = ListNode(key)  # Add the new key at the end of the list

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next  # Skip the node to remove it
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
```

### Time and Space Complexity

* **Time:** O(n/k), where n is the number of keys and k is the number of buckets.
* **Space:** O(k + m), where k is the size of the array and m is the number of nodes.

### Analysis

This method balances time and space. It handles a wide range of keys efficiently without using too much memory. It's the most optimal solution when memory is limited and key ranges are sparse.

---

## Conclusion

* **Brute Force List:** Easy to implement but slow for large datasets.
* **Boolean Array:** Fastest in time but consumes a lot of memory.
* **Linked List with Hashing:** Most balanced and scalable solution.

If memory usage is not a concern, the Boolean Array method is fastest. If efficiency and scalability are priorities, the Linked List method is the most optimal.
