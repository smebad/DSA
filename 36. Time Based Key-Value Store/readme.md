# Time Based Key-Value Store - LeetCode Problem

## Problem Description

The **Time Based Key-Value Store** problem involves designing a data structure that stores key-value pairs along with timestamps, allowing retrieval of the most recent value before or at a given timestamp. The key challenge is to support efficient insertions and queries.

### Required Operations:

1. **`set(String key, String value, int timestamp)`**

   * Store the key with the value and its corresponding timestamp.
2. **`get(String key, int timestamp)`**

   * Return the value associated with the largest timestamp <= given timestamp.
   * If no such timestamp exists, return an empty string `""`.

## Example

```python
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]
```

## Constraints

* Timestamps are strictly increasing for a given key.
* Up to `2 * 10^5` calls to `set` and `get`.

---

## Approach

To optimize `get`, we use **binary search** since all timestamps for a given key are stored in increasing order.

### Data Structure

```python
self.keyStore = {
    "key1": [[val1, timestamp1], [val2, timestamp2], ...],
    "key2": [[...]],
    ...
}
```

---

## Binary Search Array Solution (Efficient)

```python
class TimeMap:

    def __init__(self):
        # Dictionary to hold key -> list of [value, timestamp]
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key not in store, initialize list
        if key not in self.keyStore:
            self.keyStore[key] = []
        # Append the [value, timestamp] pair
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        # Binary search for the highest timestamp <= given timestamp
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]  # Save result and search right half
                l = m + 1
            else:
                r = m - 1
        return res
```

### Test Cases

```python
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))  # Output: "bar"
print(timeMap.get("foo", 3))  # Output: "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))  # Output: "bar2"
print(timeMap.get("foo", 5))  # Output: "bar2"
```

---

## Solution Comparison

### Brute Force (Not implemented here)

* Iterate from last timestamp to first and return the latest one <= timestamp.
* Time Complexity: O(n) for get

### Optimal (Implemented)

* Binary Search on sorted list of timestamps per key
* Time Complexity:

  * **Set:** O(1)
  * **Get:** O(log n)

---

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| set       | O(1)            | O(m \* n)        |
| get       | O(log n)        | O(m \* n)        |

* `m` = number of keys
* `n` = average number of timestamped values per key

### Why It's Optimal

* Set operations are constant time.
* Get operations are log-time due to binary search.
* The space complexity is linear in total number of set operations, which is optimal given the problem requirements.

---

## Conclusion

The binary search approach in the `TimeMap` class is optimal for both performance and scalability. It handles thousands of operations efficiently, meeting the O(log n) retrieval constraint imposed by the problem.

This structure is especially useful in versioned systems, time-series databases, and scenarios requiring efficient historical lookups.
