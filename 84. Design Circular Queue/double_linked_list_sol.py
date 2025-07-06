# Design Circular Queue
# Double Linked List Solution:

class ListNode:

    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
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
    
# Time Complexity: O(n) for enQueue and deQueue operations, where n is the number of elements in the queue. This is because we may need to traverse the linked list to find the correct position for insertion or deletion.
# Space Complexity: O(1) since we are using a constant amount of extra space for the pointers and the linked list nodes, regardless of the size of the queue. For each node, we store a value, a pointer to the next node, and a pointer to the previous node.
# This solution is efficient and meets the problem's constraints.


# Test Cases
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1)) # True
print(myCircularQueue.enQueue(2)) # True
print(myCircularQueue.enQueue(3)) # True
print(myCircularQueue.enQueue(4)) # False
print(myCircularQueue.Rear()) # 3
print(myCircularQueue.isFull()) # True
print(myCircularQueue.deQueue()) # True
print(myCircularQueue.enQueue(4)) # True
print(myCircularQueue.Rear()) # 4
