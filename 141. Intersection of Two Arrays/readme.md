# Intersection of Two Arrays - LeetCode

## Problem Explanation

The problem **Intersection of Two Arrays** asks us to find the common elements between two integer arrays. Each element in the result must be **unique**, and the result can be returned in any order.

### Example:

* Input: `nums1 = [1,2,2,1]`, `nums2 = [2,2]`
  Output: `[2]`

* Input: `nums1 = [4,9,5]`, `nums2 = [9,4,9,8,4]`
  Output: `[9,4]` (or `[4,9]` since order does not matter)

### Constraints:

* `1 <= nums1.length, nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 1000`

The goal is to efficiently find the intersection of the two arrays.

---

## Code Explanation

### Brute Force Solution

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for i in nums1:
            for j in nums2:
                if i == j:  # Check if element exists in both arrays
                    res.add(i)  # Add to set (ensures uniqueness)
                    break  # Stop checking further for this element
        return list(res)
```

* We compare every element of `nums1` with every element of `nums2`.
* If they match, we add it to a set (to ensure uniqueness).
* Convert the set back to a list and return it.

**Time Complexity:** O(n\*m), where `n` and `m` are lengths of `nums1` and `nums2`.
**Space Complexity:** O(n), for storing the result.

This works but is not efficient for large arrays.

---

### Hash-Set Solution

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)  # Store all elements from nums1 in a set

        res = []
        for num in nums2:
            if num in seen:  # If element is in set
                res.append(num)  # Add to result
                seen.remove(num)  # Remove to maintain uniqueness
        return res
```

* Convert `nums1` into a set for O(1) lookups.
* Traverse `nums2` and check if the number exists in the set.
* If yes, add it to the result and remove it from the set to avoid duplicates.

**Time Complexity:** O(n + m) because we traverse both arrays once.
**Space Complexity:** O(n), due to the set.

This is much more efficient than brute force.

---

### Hash-Map Solution

```python
from collections import defaultdict

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(int)
        for num in nums1:
            seen[num] = 1  # Mark element as seen

        res = []
        for num in nums2:
            if seen[num] == 1:  # If it's marked
                seen[num] = 0   # Reset to avoid duplicates
                res.append(num)
        return res
```

* Similar to the hash-set method but uses a dictionary (`defaultdict`).
* Store elements of `nums1` with a marker.
* When traversing `nums2`, check if the marker exists and update it.

**Time Complexity:** O(n + m).
**Space Complexity:** O(n), due to the dictionary.

---

## Approach and Logic Breakdown

* **Brute Force:** Compare each element of one array with every element of the other. Simple but inefficient.
* **Hash-Set:** Use a set for quick lookups and uniqueness. This is efficient and clean.
* **Hash-Map:** Similar to the set approach but uses a dictionary to track presence.

Both **Hash-Set** and **Hash-Map** approaches are optimal compared to brute force.

---

## Complexity Analysis

1. **Brute Force:**

   * Time: O(n\*m)
   * Space: O(n)
   * Not efficient for large inputs.

2. **Hash-Set:**

   * Time: O(n + m)
   * Space: O(n)
   * Fast and efficient.

3. **Hash-Map:**

   * Time: O(n + m)
   * Space: O(n)
   * Similar efficiency to hash-set but slightly more overhead.

### Most Optimal Solution

The **Hash-Set solution** is the most optimal because:

* It provides O(1) lookups.
* Requires less overhead than hash-map.
* Efficiently ensures uniqueness and handles large arrays within given constraints.