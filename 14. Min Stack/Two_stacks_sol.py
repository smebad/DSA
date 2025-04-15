# Min Stack

# Two Stacks Solution:
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
    
# Time Complexity: O(1) for all operations.
# Space Complexity: O(n) for the two stacks.
# This solution uses two stacks: one for the main stack and another to keep track of the minimum values which is more optimal than the brute force solution.

# Test Cases:
# Test Case 1:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # Expected Output: -3
minStack.pop()
print(minStack.top()) # Expected Output: 0
print(minStack.getMin()) # Expected Output: -2
