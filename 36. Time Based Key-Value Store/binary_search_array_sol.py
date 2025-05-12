# Time Based Key-Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 

# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.


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
