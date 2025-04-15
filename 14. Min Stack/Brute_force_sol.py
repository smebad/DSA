# Min Stack

# Brute Force Solution:
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
    
# Time Complexity: O(n) for getMin, O(1) for push, pop, and top.
# Space Complexity: O(n) for getMin and O(1) for other operations.
# This solution is not optimal as it does not satisfy the O(1) time complexity requirement for getMin.
# However, it is a brute force solution that works correctly.

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
