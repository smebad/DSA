#  Design HashMap
# Array Solution:
class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

# Time Complexity: O(1) for put, get, and remove operations. This is because we are directly accessing the index in the array.
# Space Complexity: O(n) where n is the size of the array (1000001 in this case). This is the space used to store the values for keys from 0 to 1000000.
# This array based implementation is efficient in terms of time complexity but uses a lot of space.


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
