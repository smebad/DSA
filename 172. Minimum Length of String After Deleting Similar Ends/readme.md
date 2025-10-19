# Minimum Length of String After Deleting Similar Ends - LeetCode

## Problem Explanation

The problem **"Minimum Length of String After Deleting Similar Ends"** asks us to repeatedly remove matching prefixes and suffixes from a given string `s` as long as they meet these conditions:

1. Both the prefix and suffix consist of the same repeating character (e.g., all `'a'`, all `'b'`, or all `'c'`).
2. The prefix and suffix characters are the same.
3. The prefix and suffix **do not overlap**.

After performing this operation as many times as possible, we must return the **minimum length** of the remaining string.

### Example Walkthrough

#### Example 1:

Input: `s = "ca"`

* There is no prefix and suffix that are the same.
* Result: `2`

#### Example 2:

Input: `s = "cabaabac"`
Steps:

* Remove prefix `c` and suffix `c` → `abaaba`
* Remove prefix `a` and suffix `a` → `baab`
* Remove prefix `b` and suffix `b` → `aa`
* Remove prefix `a` and suffix `a` → `` (empty string)
* Result: `0`

#### Example 3:

Input: `s = "aabccabba"`
Steps:

* Remove prefix `aa` and suffix `a` → `bccabb`
* Remove prefix `b` and suffix `bb` → `cca`
* No further operations possible.
* Result: `3`

---

## Code with Comments

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize two pointers: left (l) at the start and right (r) at the end
        l, r = 0, len(s) - 1

        # Continue while the left pointer is before the right and both ends match
        while l < r and s[l] == s[r]:
            tmp = s[l]  # Store the current matching character

            # Move the left pointer forward as long as characters match 'tmp'
            while l <= r and s[l] == tmp:
                l += 1

            # Move the right pointer backward as long as characters match 'tmp'
            while l <= r and s[r] == tmp:
                r -= 1

        # Return the remaining length of the string
        return r - l + 1
```

---

## Approach and Logic

This solution uses the **Two-Pointer Technique**:

1. **Initialization**: Set `l` (left) to the start of the string and `r` (right) to the end.
2. **Compare Ends**: Check if `s[l]` equals `s[r]`.

   * If they are different, we cannot remove anything; return the length.
   * If they are the same, store that character in `tmp`.
3. **Skip Matching Characters**:

   * Move `l` forward while `s[l] == tmp`.
   * Move `r` backward while `s[r] == tmp`.
4. **Repeat** until the two ends no longer match.
5. **Compute the Remaining Length**: After the loop ends, the remaining string length is `r - l + 1`.

### Intuition

* You always remove matching sequences from both ends.
* Since each operation strictly reduces the string’s size, it guarantees termination.
* The use of two pointers makes the process efficient by avoiding unnecessary string creation.

---

## Complexity Analysis

### Time Complexity: **O(n)**

* Each character in the string is visited **at most once** by either `l` or `r`.
* Thus, the algorithm runs in **linear time**, where `n` is the length of `s`.

### Space Complexity: **O(1)**

* Only a few variables (`l`, `r`, `tmp`) are used, requiring **constant extra space**.

---

## Why This is Optimal

* Any approach that simulates actual string deletion (e.g., using slicing or concatenation) would take **O(n²)** time due to string copying.
* This **two-pointer** solution avoids that entirely by working with indices only.
* Therefore, it achieves the **most optimal time and space complexity** possible for this problem.

---

## Test Cases

```python
# Test Case 1
print(Solution().minimumLength('ca'))  # Expected Output: 2

# Test Case 2
print(Solution().minimumLength('cabaabac'))  # Expected Output: 0

# Test Case 3
print(Solution().minimumLength('aabccabba'))  # Expected Output: 3
```