# Time Based Key-Value Store
# Binary Search Array Solution:

class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    
# Time Complexity: O(1) for set, O(log n) for get, where n is the number of values stored for the key.
# Space Complexity: O(m * n), where m is the number of keys and n is the average number of values stored for each key.
# The space complexity is O(m * n) because we are storing m keys, and each key can have up to n values.
# This binary search array solution is efficient for both time and space complexity, making it suitable for large datasets.
# The binary search approach allows for efficient retrieval of values based on timestamps, while the dictionary structure provides quick access to the key-value pairs.
# The approach is optimal for scenarios where the number of keys is large, and the number of values per key is also significant.


# Test Cases:
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))  # return "bar"
print(timeMap.get("foo", 3))  # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))  # return "bar2"
print(timeMap.get("foo", 5))  # return "bar2"
# Output: [null, null, "bar", "bar", null, "bar2", "bar2"]
