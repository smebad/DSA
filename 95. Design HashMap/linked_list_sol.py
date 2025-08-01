#  Design HashMap
# Linked List Solution:
class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
    
    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Time Complexity: O(n / k) for put, get, and remove operations, where n is the number of elements in the hashmap and k is the number of buckets (1000 in this case). This is because we may need to traverse a linked list in the worst case.
# Space Complexity: O(k + m) where k is the number of buckets (1000) and m is the number of elements in the hashmap. Each bucket contains a linked list of nodes, and we use additional space for each node.
# This linked list based implementation is more space-efficient than the array-based one, especially when the number of keys is much smaller than the size of the array. It also handles collisions by chaining, which allows multiple key-value pairs to be stored in the same bucket.



# Test Case:
myHashMap = MyHashMap()
myHashMap.put(1, 1)  # The map is now [[1,1]]
myHashMap.put(2, 2)  # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))  # Output: 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))  # Output: -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1)  # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))  # Output: 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2)  # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))  # Output: -1 (i.e., not found), The map is now [[1,1]]
