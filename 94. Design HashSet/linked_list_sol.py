# Design HashSet
# Linked List Solution:
class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

# Time Complexity: O(n/k) where n is the number of elements in the set and k is the size of the hash table. This is because we are iterating through the hash table once.
# Space Complexity: O(k + m) where k is the size of the hash table and m is the number of elements in the set. This is because we are storing the hash table and the set in memory.
# This linked list solution is efficient in both time and space. 

# Test Cases
# Test Case 1:
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))  # Output: True
print(myHashSet.contains(3))  # Output: False
myHashSet.add(2)
print(myHashSet.contains(2))  # Output: True
myHashSet.remove(2)
print(myHashSet.contains(2))  # Output: False
