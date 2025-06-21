# Implement Stack using Queues - LeetCode

## Problem Description

The **Implement Stack using Queues** problem asks us to simulate the behavior of a stack (Last-In-First-Out, LIFO) using only the operations permitted for a queue. A stack should support the following operations:

* `push(x)`: Push element `x` onto the stack.
* `pop()`: Remove the element on the top of the stack and return it.
* `top()`: Return the element on the top of the stack.
* `empty()`: Return whether the stack is empty.

### Constraints:

* Only standard queue operations can be used: push to back, pop from front, peek from front, size, and is empty.
* Implementations may simulate a queue using a deque (double-ended queue), but must adhere to queue rules.

---

## One Queue Solution

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()  # initialize a single queue

    def push(self, x: int) -> None:
        self.q.append(x)  # enqueue the new element
        # rotate the queue so the new element is at the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()  # dequeue the front element (top of stack)

    def top(self) -> int:
        return self.q[0]  # peek the front element (top of stack)

    def empty(self) -> bool:
        return len(self.q) == 0  # check if queue is empty
```

### Explanation of Code

* The `push` operation enqueues the element and then rotates the queue to place the new element at the front. This ensures that the most recently pushed element will be the first to be dequeued.
* `pop` simply dequeues the front element.
* `top` peeks at the front of the queue.
* `empty` checks if the queue is empty.

---

## Approach and Logic

* A queue follows First-In-First-Out (FIFO), while a stack requires Last-In-First-Out (LIFO) behavior.
* To emulate LIFO using a queue, the key is to reverse the order of elements upon each push.
* This is achieved by rotating the queue right after appending a new element.
* The rotation moves the newly added element to the front, allowing `pop()` and `top()` to operate in constant time.

---

## Time and Space Complexities

### Time Complexity:

* `push`: O(n), where n is the number of elements in the stack (due to rotation)
* `pop`: O(1)
* `top`: O(1)
* `empty`: O(1)

### Space Complexity:

* O(n), where n is the number of elements in the stack (stored in a single queue)

### Which is Optimal?

* This solution is optimal for the follow-up requirement to use only one queue.
* It sacrifices push performance (O(n)) for faster pop and top operations (O(1)).
* Ideal when push is less frequent than pop or top.

---

## Test Cases

```python
# Test Case 1
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())    # Expected Output: 2
print(myStack.pop())    # Expected Output: 2
print(myStack.empty())  # Expected Output: False

# Test Case 2
myStack = MyStack()
print(myStack.empty())  # Expected Output: True
```
