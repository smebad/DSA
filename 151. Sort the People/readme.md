# Sort the People - LeetCode

## Problem Explanation

The problem "Sort the People" requires sorting a list of people based on their heights. You are given two arrays:

* **names**: an array of strings representing the names of people.
* **heights**: an array of distinct positive integers representing the heights of those people.

Both arrays have the same length, and each index `i` corresponds to one person, meaning `names[i]` belongs to the person with height `heights[i]`.

**Goal:** Return the list of names sorted in descending order of heights.

### Example 1

**Input:**

```python
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
```

**Output:**

```python
["Mary", "Emma", "John"]
```

**Explanation:** Mary is the tallest (180), followed by Emma (170), then John (165).

### Example 2

**Input:**

```python
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
```

**Output:**

```python
["Bob", "Alice", "Bob"]
```

**Explanation:** The first Bob is the tallest (185), followed by Alice (155), and then the second Bob (150).

---

## (Hashmap + Sorting)

```python
from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Create a mapping of height -> name
        height_to_name = {}
        for h, n in zip(heights, names):
            height_to_name[h] = n

        res = []
        # Sort heights in descending order and retrieve names accordingly
        for h in reversed(sorted(heights)):
            res.append(height_to_name[h])

        return res
```

### Code Explanation with Comments

1. **Mapping heights to names**:

   ```python
   height_to_name = {}
   for h, n in zip(heights, names):
       height_to_name[h] = n
   ```

   * We use a dictionary to store each height as a key and its corresponding name as a value.
   * Example: `{180: "Mary", 165: "John", 170: "Emma"}`.

2. **Sorting heights in descending order**:

   ```python
   for h in reversed(sorted(heights)):
       res.append(height_to_name[h])
   ```

   * We sort the `heights` list in ascending order, then reverse it for descending order.
   * For each height, we append its mapped name to the result list.

3. **Returning the result**:

   * After appending all names according to sorted heights, we return the final list of names.

---

## Approach and Logic

* The key idea is that sorting must be based on `heights`, but the result should return corresponding `names`.
* A dictionary (`height_to_name`) makes it easy to retrieve names once heights are sorted.
* Sorting the heights ensures the order requirement is met.

## Time and Space Complexity

### Time Complexity

* Creating the hashmap takes **O(n)** time.
* Sorting the heights takes **O(n log n)** time.
* Appending names based on sorted heights takes **O(n)** time.
* **Overall:** **O(n log n)**, dominated by sorting.

### Space Complexity

* Dictionary `height_to_name` stores all `n` mappings.
* Result list stores `n` names.
* **Overall:** **O(n)**.

---

## Optimal Solution

The provided solution is optimal for this problem:

* Sorting is unavoidable because the names must be ordered by height.
* Thus, **O(n log n)** time is the best possible.
* Space usage is linear (**O(n)**), which is acceptable given problem constraints.

This makes the hashmap + sorting solution both simple and efficient.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
print(sol.sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]

# Test Case 2
names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(sol.sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]
```