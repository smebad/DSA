# Optimal Partition of String - LeetCode

## 1. Problem Explanation

The **Optimal Partition of String** problem requires dividing a given string into the smallest possible number of substrings. Each substring must contain **only unique characters**, meaning no character is allowed to repeat within the same substring.

Every character from the string must be included in exactly one substring.

### Example

* Input: `"abacaba"`
* Output: `4`

A valid partition is:

* ("a", "ba", "cab", "a")

The goal is to minimize the number of resulting substrings.

---

## 2. Code with Explanations

```python
class Solution:
    def partitionString(self, s: str) -> int:
        curSet = set()        # Keeps track of characters in the current substring
        res = 1               # At least one substring is always needed

        for c in s:
            if c in curSet:   # If character already exists, start a new substring
                res += 1      # Increase substring count
                curSet.clear()# Reset for the new substring

            curSet.add(c)     # Add current character to the new/ongoing substring

        return res            # Minimum number of substrings
```

### What the Code Does

* Uses a **set** to track characters currently in the active substring.
* If a character repeats, a new substring must be started.
* Counts how many such partitions are needed.

---

## 3. Solution Approach and Logic

### Idea

We want **each substring to have all unique letters**. If a character repeats, we cannot keep it in the same substring.

So, the strategy is:

1. Move through the string left to right.
2. Build a substring until a character repeats.
3. When a repeat is detected, start a new substring.
4. Count how many such substrings are formed.

### Why This Works

This method ensures:

* Each substring has no duplicates.
* We only create a new substring when absolutely needed.

This is why the number of substrings is **minimal**.

### Example Walkthrough

String: `"abacaba"`

* Start with substring 1: `a`
* Add `b` → `ab`
* See `a` again → start substring 2: `a`
* Add `c` → `ac`
* See `a` again → start substring 3: `a`
* Add `b` → `ab`
* See `a` again → start substring 4: `a`

Total substrings = 4.

This is the smallest possible.

---

## 4. Time and Space Complexity

### Time Complexity: **O(n)**

* The string is scanned once.
* All operations inside the loop are constant time.

### Space Complexity: **O(1)**

* The `set` can have at most 26 lowercase letters.
* So the memory used never grows with input size.

### Why This Is Optimal

* You must look at every character at least once, so you cannot do better than **O(n)**.
* Using a fixed-size set means no extra memory scales with input, making it optimal in space as well.

This makes the HashSet approach the most efficient solution possible for this problem.

---

## 5. Test Cases
```python
sol = Solution()

# Test Case 1:
s1 = "abacaba"
print(sol.partitionString(s1))  # Expected output: 4

# Test Case 2:
s2 = "ssssss"
print(sol.partitionString(s2))  # Expected output: 6
```