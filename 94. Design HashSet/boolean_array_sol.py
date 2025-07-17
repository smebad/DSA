# Design HashSet
# Boolean Array Solution:
class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
    
# Time Complexity: O(1) because the size of the hash table is fixed. 
# Space Complexity: O(1000000) because the size of the hash table is fixed. This is the maximum possible size of the hash table.
# This boolean array solution is more memory efficient than the brute force solution. 

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
