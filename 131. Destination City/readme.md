# Destination City - LeetCode

## Problem Explanation

The **Destination City** problem comes from LeetCode. You are given an array `paths`, where each element `paths[i] = [cityAi, cityBi]` represents a direct path from city `cityAi` to city `cityBi`.

The task is to return the **destination city** — the city that has **no outgoing paths** to any other city.

It is guaranteed that the graph formed by the paths is a straight line (no loops), so there will be exactly **one unique destination city**.

### Example

**Input:**

```python
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
```

**Output:**

```python
"Sao Paulo"
```

**Explanation:** The trip is: London → New York → Lima → Sao Paulo. The last city "Sao Paulo" has no outgoing path, so it is the destination city.

---

## Provided Solutions

### 1. Hash-Set Solution

```python
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        # Step 1: Add all starting cities (cityAi) into a set
        for p in paths:
            s.add(p[0])

        # Step 2: Check destination cities (cityBi). If a city is not in set, it has no outgoing path
        for p in paths:
            if p[1] not in s:
                return p[1]
```

**Explanation:**

* First, store all starting cities in a set.
* Then, loop through each path's destination city (`cityBi`).
* If a destination city is not in the set, it means no path starts from it — so it is the destination city.

**Time Complexity:** `O(n)` where `n` is the number of paths. We iterate twice over the list.
**Space Complexity:** `O(n)` for storing all starting cities.

---

### 2. Hash-Map Solution

```python
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Step 1: Create a map from start city -> destination city
        mp = {p[0]: p[1] for p in paths}

        # Step 2: Start from the first city, keep moving forward until no outgoing path exists
        start = paths[0][0]
        while start in mp:
            start = mp[start]
        return start
```

**Explanation:**

* Create a dictionary where each starting city points to its destination.
* Begin from the first path's starting city.
* Keep following the chain until you reach a city that does not appear as a key in the map.
* That city is the destination city.

**Time Complexity:** `O(n)` where `n` is the number of paths. Each city is visited once.
**Space Complexity:** `O(n)` for storing the map of paths.

---

## Approaches Explained in Simple Words

* **Hash-Set Method:** Think of it like writing down all "departing cities" on a list. Then check each "arriving city". If the arriving city is never listed as a departing city, that’s your final destination.
* **Hash-Map Method:** Imagine following the path step by step. From the first city, go to the next. Keep walking until you can’t go further — that last stop is your destination.

Both approaches give the same correct answer, but they differ in style:

* The **Hash-Set solution** looks for a city that no one leaves from.
* The **Hash-Map solution** follows the trip step by step until the end.

---

## Complexity Analysis

* **Hash-Set Solution:**

  * Time: `O(n)` (loop twice over paths)
  * Space: `O(n)` (store starting cities)

* **Hash-Map Solution:**

  * Time: `O(n)` (traverse map once)
  * Space: `O(n)` (store all city mappings)

Both are equally efficient in time and space for this problem. However:

* The **Hash-Set method** is slightly simpler and more direct.
* The **Hash-Map method** is more intuitive if you think of traveling along the path.

### Most Optimal Solution

Both methods are optimal (`O(n)` time, `O(n)` space). Since input size is small (`<= 100` paths), either is perfectly efficient. If simplicity is preferred, the **Hash-Set solution** is often the goto.