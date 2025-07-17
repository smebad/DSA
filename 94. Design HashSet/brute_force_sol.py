# Design HashSet
# Brute Force Solution:
class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data
    
# Time Complexity: O(n) for add, remove, and contains, where n is the number of elements in the set. 
# Space Complexity: O(n) for the data list, where n is the number of elements in the set.
# This brute force solution is simple but can be slow for large sets.

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
