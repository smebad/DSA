# Implement Stack using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
 

# Follow-up: Can you implement the stack using only one queue?


# One queue solution:
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
    
# Time Complexity: O(1) for pop and top, O(n) for push where n is the number of elements in the stack.
# Space Complexity: O(n) where n is the number of elements in the stack.
# In this implementation, we use a single queue to simulate the stack behavior. When we push an element, we append it to the queue and then rotate the queue so that the newly added element is at the front. This way, pop and top operations can be performed in O(1) time. The space complexity remains O(n) due to the storage of elements in the queue.
# However, the push operation takes O(n) time because we need to rotate the queue to maintain the stack order. This solution is efficient for scenarios where the number of push operations is relatively small compared to pop and top operations.
# This solution is optimal for the follow-up question, as it uses only one queue to implement the stack functionality. The key idea is to maintain the order of elements such that the last pushed element is always at the front of the queue, allowing for efficient pop and top operations.


# Test cases
# Test Case 1:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top()) # Expected Output: 2
print(myStack.pop()) # Expected Output: 2
print(myStack.empty()) # Expected Output: False

# Test Case 2:
myStack = MyStack()
print(myStack.empty()) # Expected Output: True