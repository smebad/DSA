# Implement Queue using Stacks - LeetCode

## Problem Description

The **Implement Queue using Stacks** problem asks us to simulate the behavior of a First In First Out (FIFO) queue using only standard stack operations.

We must implement the following methods:

* `push(x)`: Push element `x` to the back of the queue.
* `pop()`: Remove and return the element from the front of the queue.
* `peek()`: Return the element at the front of the queue.
* `empty()`: Return `True` if the queue is empty, else `False`.

**Constraints:**

* Only standard stack operations are allowed: `push`, `pop`, `peek`, `size`, and `isEmpty`.
* At most 100 operations will be called.

---

## Two Stacks Solution

```python
class MyQueue:
    def __init__(self):
        self.s1 = []  # Main input stack
        self.s2 = []  # Helper output stack

    def push(self, x: int) -> None:
        # Push the element to input stack
        self.s1.append(x)

    def pop(self) -> int:
        # Move elements to output stack if empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Pop from output stack which simulates front of queue
        return self.s2.pop()

    def peek(self) -> int:
        # Move elements to output stack if empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Peek from output stack to get front element
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.s1 and not self.s2
```

---

## Explanation of Code

* We use two stacks: `s1` for pushing elements and `s2` for popping/peeking.
* On `push`, we simply add the element to `s1`.
* On `pop` or `peek`, if `s2` is empty, we move all elements from `s1` to `s2` to reverse their order. This makes the oldest element accessible for FIFO.
* `empty` checks if both stacks are empty.

---

## Approach and Logic

This method cleverly uses the **LIFO** nature of stacks to simulate **FIFO** behavior:

* By reversing elements from `s1` into `s2`, we turn the newest elements to the bottom and oldest to the top of `s2`.
* This lets `s2.pop()` or `s2[-1]` simulate queue front operations.
* The reversal only happens when `s2` is empty, so it's not repeated unnecessarily.

---

## Time and Space Complexities

* **Time Complexity**:

  * `push`: O(1)
  * `pop`: Amortized O(1), worst-case O(n)
  * `peek`: Amortized O(1), worst-case O(n)
  * `empty`: O(1)

* **Space Complexity**: O(n), where `n` is the number of elements in the queue (combined in both stacks).

**Why is it optimal?**

* Each element is moved between stacks at most once, resulting in amortized constant time per operation.
* This satisfies the follow-up constraint of achieving O(1) time on average.

---

## Test Cases

```python
# Test Case 1
myQueue = MyQueue()
myQueue.push(1)  # Queue is: [1]
myQueue.push(2)  # Queue is: [1, 2]
print(myQueue.peek())  # Output: 1
print(myQueue.pop())   # Output: 1
print(myQueue.empty()) # Output: False

# Test Case 2
myQueue = MyQueue()
print(myQueue.empty()) # Output: True
```