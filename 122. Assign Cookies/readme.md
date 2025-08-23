# Assign Cookies - LeetCode

## Problem Explanation

The **Assign Cookies** problem is a greedy algorithm problem. You are given:

* An array `g` where `g[i]` represents the *greed factor* of the `i-th` child. This is the minimum size of a cookie the child will accept.
* An array `s` where `s[j]` represents the size of the `j-th` cookie.

Each child can receive **at most one cookie**, and a child will only be content if the cookie size is **greater than or equal to** their greed factor. The goal is to maximize the number of content children.

### Example 1

**Input:**

```text
g = [1,2,3]
s = [1,1]
```

**Output:**

```text
1
```

**Explanation:** Only the child with greed factor `1` can be satisfied, since both cookies are of size `1`.

### Example 2

**Input:**

```text
g = [1,2]
s = [1,2,3]
```

**Output:**

```text
2
```

**Explanation:** Both children can be satisfied with cookie sizes `1` and `2`.

---

## Two-Pointers Solution

```python
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Step 1: Sort both greed factors and cookie sizes
        g.sort()
        s.sort()

        # i -> pointer for children
        # j -> pointer for cookies
        i = j = 0

        # Step 2: Traverse through children and cookies
        while i < len(g) and j < len(s):
            # If the current cookie can satisfy the current child
            if g[i] <= s[j]:
                i += 1  # Move to the next child
            # Whether satisfied or not, move to the next cookie
            j += 1

        # Step 3: Return number of satisfied children
        return i
```

---

## Approach and Logic

### Greedy + Two Pointers Approach

1. **Sort both arrays:**

   * Sorting ensures that we start with the smallest greed child and the smallest cookie.
   * This way, we avoid "wasting" a large cookie on a less greedy child.

2. **Use two pointers:**

   * Pointer `i` tracks children.
   * Pointer `j` tracks cookies.

3. **Assign cookies:**

   * If `s[j] >= g[i]`, it means the cookie can satisfy the child:

     * Move to the next child (`i += 1`).
   * Always move to the next cookie (`j += 1`).

4. **Stop condition:**

   * When we run out of either children or cookies.

5. **Result:**

   * The value of `i` tells us how many children were satisfied.

### Why This Works

This is a **greedy algorithm**:

* We always try to satisfy the least greedy child first with the smallest possible cookie.
* This ensures that larger cookies are saved for greedier children, maximizing the total number of satisfied children.

---

## Complexity Analysis

### Time Complexity

* Sorting `g`: **O(n log n)**
* Sorting `s`: **O(m log m)**
* Traversal using two pointers: **O(n + m)**
* **Overall:** `O(n log n + m log m)`

  * Where `n` is the number of children and `m` is the number of cookies.

### Space Complexity

* Sorting in Python uses **O(1)** or **O(n + m)** depending on the implementation.
* Apart from sorting, only constant extra variables are used.
* **Overall:** `O(1)` extra space.

### Most Optimal Solution

The **two pointers + greedy approach** is the most optimal:

* Sorting is unavoidable since we need to match cookies and greed factors efficiently.
* After sorting, the two-pointer method ensures that we maximize satisfaction in a single pass.
* Thus, `O(n log n + m log m)` time and `O(1)` space is the best we can achieve.