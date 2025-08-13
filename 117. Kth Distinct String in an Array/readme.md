# Kth Distinct String in an Array - LeetCode

## Problem Description

A **distinct string** is a string that appears **only once** in an array.

Given:

* An array of strings `arr`.
* An integer `k`.

Return the **k-th distinct string** present in `arr`. If there are fewer than `k` distinct strings, return an empty string `""`.

The strings are considered in the **order they appear** in the array.

---

### Example 1:

**Input:**

```python
arr = ["d", "b", "c", "b", "c", "a"]
k = 2
```

**Output:**

```
"a"
```

**Explanation:**

* Distinct strings are `["d", "a"]`.
* `"d"` is the 1st distinct, `"a"` is the 2nd distinct.
* Since `k = 2`, return `"a"`.

### Example 2:

**Input:**

```python
arr = ["aaa", "aa", "a"]
k = 1
```

**Output:**

```
"aaa"
```

**Explanation:**

* All strings are distinct.
* The 1st distinct string is `"aaa"`.

### Example 3:

**Input:**

```python
arr = ["a", "b", "a"]
k = 3
```

**Output:**

```
""
```

**Explanation:**

* Only distinct string is `"b"`.
* Fewer than 3 distinct strings, so return `""`.

**Constraints:**

```
1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
```

---

## Brute-Force Solution

```python
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            flag = True  # Assume arr[i] is distinct unless proven otherwise
            
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j]:  # Found a duplicate
                    flag = False
                    break
            
            if flag:  # arr[i] is distinct
                k -= 1
                if k == 0:
                    return arr[i]
        return ""
```

### How it works:

1. For each string, check if it appears anywhere else.
2. If it does not, it is distinct.
3. Keep counting distinct strings until the k-th one is found.
4. Return `""` if fewer than k distinct strings exist.

**Time Complexity:** `O(n^2)` — Nested loops for comparisons.

**Space Complexity:** `O(1)` — Only a few variables used.

---

## Hash-Map Solution (Efficient)

```python
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}  # Dictionary to store frequency of each string
        
        # Count occurrences
        for s in arr:
            if s not in count:
                count[s] = 0
            count[s] += 1
        
        # Find k-th distinct in original order
        for s in arr:
            if count[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
```

### How it works:

1. Count how many times each string appears.
2. Loop through the array in order and check for strings with frequency `1`.
3. Decrease `k` until the k-th distinct string is found.

**Time Complexity:** `O(n)` — One pass for counting, one pass for finding.

**Space Complexity:** `O(n)` — Dictionary stores counts.

---

## Hash-Set Solution

```python
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct, seen = set(), set()
        
        # Identify distinct strings
        for s in arr:
            if s in distinct:
                distinct.remove(s)
                seen.add(s)
            elif s not in seen:
                distinct.add(s)
        
        # Find k-th distinct in order
        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s
        return ""
```

### How it works:

1. Use two sets:

   * `distinct` for strings that have appeared once.
   * `seen` for strings that appeared more than once.
2. Update sets as you iterate.
3. Loop again to find the k-th distinct in order.

**Time Complexity:** `O(n)` — Two passes over the array.

**Space Complexity:** `O(n)` — Sets store distinct and seen strings.

---

## Differences Between Solutions

| Aspect                | Brute Force Solution       | Hash-Map Solution    | Hash-Set Solution         |
| --------------------- | -------------------------- | -------------------- | ------------------------- |
| Time Complexity       | `O(n^2)` (slow)            | `O(n)` (fast)        | `O(n)` (fast)             |
| Space Complexity      | `O(1)`                     | `O(n)`               | `O(n)`                    |
| Ease of Understanding | Easy                       | Medium               | Medium                    |
| Practical Use         | Only for very small arrays | Best for general use | Also good for general use |

**Why Hash-Map is Optimal:**

* It is straightforward and fast — only needs two passes.
* It directly stores counts without needing to manage multiple sets.

---

## Key Takeaways

* The k-th distinct string is found by counting how often each string appears and then checking order.
* Brute force is simple but too slow for larger arrays.
* Hash-map is usually the cleanest and most efficient approach.
* Hash-set is also efficient but slightly more complex in logic.
