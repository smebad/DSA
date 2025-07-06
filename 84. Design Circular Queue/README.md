# Design Circular Queue - LeetCode

## Problem Description

The goal is to implement a **circular queue**, which is a linear data structure that follows the **FIFO (First In First Out)** principle and connects the last position back to the first to form a circle (also known as a ring buffer).

A circular queue optimizes the use of storage by reusing the space vacated by dequeued elements.

You need to design a class `MyCircularQueue` with the following operations:

* `MyCircularQueue(k)`: Initializes the queue with size `k`.
* `enQueue(value)`: Inserts an element into the circular queue. Returns `True` if the operation is successful.
* `deQueue()`: Deletes an element from the circular queue. Returns `True` if the operation is successful.
* `Front()`: Gets the front item from the queue. Returns `-1` if the queue is empty.
* `Rear()`: Gets the last item from the queue. Returns `-1` if the queue is empty.
* `isEmpty()`: Checks whether the circular queue is empty.
* `isFull()`: Checks whether the circular queue is full.

### Constraints

* 1 <= `k` <= 1000
* 0 <= `value` <= 1000
* At most 3000 function calls will be made.

---

## Code Explanation with Comments

```python
class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k  # number of available spots
        self.left = ListNode(0, None, None)  # dummy left (front sentinel)
        self.right = ListNode(0, None, self.left)  # dummy right (rear sentinel)
        self.left.next = self.right  # connect left to right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        # create a new node and insert it before the rear sentinel
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1  # decrease available space
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        # remove the node right after the front sentinel
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1  # increase available space
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0
```

---

## Approach and Logic

This implementation uses a **doubly linked list** with two sentinel nodes (`left` and `right`) to simplify insertions and deletions at the ends.

### Why Doubly Linked List?

* Avoids the need to shift elements manually as in an array.
* Insertion and deletion at both ends are constant time operations (amortized).

### Operations:

* `enQueue`: Adds a node before the `right` sentinel.
* `deQueue`: Removes the node after the `left` sentinel.
* `Front`/`Rear`: Returns the value of the node next to `left` or before `right`.
* `isFull`/`isEmpty`: Uses the `space` counter to determine state.

---

## Time and Space Complexities

* **Time Complexity**:

  * `enQueue`: O(1)
  * `deQueue`: O(1)
  * `Front`/`Rear`: O(1)
  * `isEmpty`/`isFull`: O(1)
* **Space Complexity**: O(k), where k is the maximum number of elements allowed in the queue.

### Why It Is Optimal

* All operations are constant time.
* Space is limited to the size of the queue (`k`), no unused memory is wasted.
* The use of sentinel nodes simplifies pointer logic and avoids edge cases.

---

## Example Usage

```python
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # True
print(myCircularQueue.enQueue(2))  # True
print(myCircularQueue.enQueue(3))  # True
print(myCircularQueue.enQueue(4))  # False (queue is full)
print(myCircularQueue.Rear())      # 3
print(myCircularQueue.isFull())    # True
print(myCircularQueue.deQueue())   # True
print(myCircularQueue.enQueue(4))  # True
print(myCircularQueue.Rear())      # 4
```
