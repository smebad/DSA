# Implement Queue using Stacks
# Two Stacks Solution:

class MyQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0
    
# Time Complexity: O(1) for push, O(n) for pop and peek in the worst case when s2 is empty, O(1) for empty. This is because we may need to transfer all elements from s1 to s2. The amortized time complexity for pop and peek is O(1) since each element is moved between the stacks at most once.
# Space Complexity: O(n) where n is the number of elements in the queue, as we are using two stacks to store the elements.
# This solution uses two stacks to simulate the behavior of a queue, ensuring that the first element pushed is the first one popped, maintaining FIFO order. And it efficiently handles the operations by transferring elements between the stacks only when necessary, achieving amortized O(1) time complexity for pop and peek operations.


# Test Cases
# Test Case 1:
myQueue = MyQueue()
myQueue.push(1)  # Queue is: [1]
myQueue.push(2)  # Queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())  # return 1
print(myQueue.pop())  # return 1, queue is [2]
print(myQueue.empty())  # return false

# Test Case 2:
myQueue = MyQueue()
print(myQueue.empty())  # return true
