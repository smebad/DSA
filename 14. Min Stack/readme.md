# Min Stack

## Problem Description
The **Min Stack** problem involves designing a stack data structure that supports the following operations in constant time:

- `push(int val)`: Pushes an element onto the stack.
- `pop()`: Removes the top element from the stack.
- `top()`: Retrieves the top element.
- `getMin()`: Retrieves the minimum element in the stack.

The challenge is to ensure that all operations, especially `getMin()`, run in constant **O(1)** time.

### Constraints:
- −231 <= val <= 231 - 1
- All operations will be called on non empty stacks.
- At most 30,000 operations will be performed.

## Example
```python
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # Returns -3
minStack.pop()
minStack.top()    # Returns 0
minStack.getMin() # Returns -2
```

---

## Solution 1: Brute Force
```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return mini
```

### Explanation
- `push`: Adds an element to the stack.
- `pop`: Removes the last element.
- `top`: Returns the last element.
- `getMin`: Traverses the stack to find the minimum. It temporarily removes all elements to compute the minimum and then restores the stack.

### Time Complexity
- `push`, `pop`, `top`: O(1)
- `getMin`: O(n) (Not optimal for large inputs)

### Space Complexity
- `O(n)` due to temporary list used during `getMin`.

---

## Solution 2: Optimal - Two Stacks
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

### Explanation
- Two stacks are maintained:
  - `stack`: for storing all values.
  - `minStack`: for storing the minimum value at every point.
- On `push`, we add to both stacks. `minStack` holds the minimum of the current value and the last min.
- On `pop`, both stacks are popped.
- `top` returns the top of the main stack.
- `getMin` returns the top of the `minStack`, which is always the minimum.

### Time Complexity
- All operations: O(1)

### Space Complexity
- O(n) for storing values and corresponding minimums.

### Optimality
This is the most optimal solution. It maintains constant time operations for all required methods and avoids unnecessary traversal by using an auxiliary stack.

---

## Test Cases
```python
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # Output: -3
minStack.pop()
print(minStack.top())    # Output: 0
print(minStack.getMin()) # Output: -2
```

---

## Summary
The Min Stack problem challenges the developer to manage state efficiently using stacks. The brute force method works but fails to meet performance expectations for large input sizes. The two stack approach is efficient and meets all constraints with O(1) time complexity for every operation.

