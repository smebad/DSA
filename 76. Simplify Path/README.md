# Simplify Path - LeetCode

## Problem Description

The **Simplify Path** problem asks us to simplify a Unix-style absolute file path string to its canonical path format.

### Rules for Simplification:

* A single period `.` refers to the current directory and can be ignored.
* A double period `..` refers to going one level up (parent directory).
* Multiple consecutive slashes `//` are treated as a single slash.
* Any other string is a valid directory or file name, including sequences like `...` or `....`.
* The result must:

  * Start with a single slash `/`.
  * Have directories separated by one slash `/`.
  * Not end with a slash unless it is the root `/`.
  * Not contain any `.` or `..` in the final path.

---

## Code Implementation

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []           # Stack to keep valid directory names
        cur = ""             # Temporary string to build directory names

        for c in path + "/":  # Append slash to handle the last segment uniformly
            if c == "/":
                if cur == "..":         # Go one level up
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":  # Valid directory name
                    stack.append(cur)
                cur = ""   # Reset current
            else:
                cur += c    # Build current segment

        return "/" + "/".join(stack)  # Construct simplified path
```

---

## Solution Explanation

### Approach:

* Use a **stack** to simulate traversal of directories.
* Iterate through the path and split it into components by detecting slashes.
* For each component:

  * Ignore empty segments or `.` (current directory).
  * Pop from the stack if `..` is found (go back one directory).
  * Otherwise, push valid directory names to the stack.
* Reconstruct the final simplified path from the stack.

### Why Stack?

* The stack provides a natural way to process directories in a LIFO manner, making it easy to handle `..` by popping the last valid directory.

---

## Time and Space Complexity

* **Time Complexity**: `O(n)` where `n` is the length of the input path. We iterate through each character once.
* **Space Complexity**: `O(n)` in the worst case where all segments are valid directory names.

### Optimality

This solution is optimal because:

* It handles all edge cases in a single pass.
* It maintains a minimal amount of state using a single stack.
* No redundant processing or multiple passes through the path are required.

---

## Test Cases

```python
# Test case 1:
input1 = "/home/"
output1 = "/home"
result1 = Solution().simplifyPath(input1)
print("Test case 1:", "Passed" if result1 == output1 else f"Failed (Got {result1})")

# Test case 2:
input2 = "/home//foo/"
output2 = "/home/foo"
result2 = Solution().simplifyPath(input2)
print("Test case 2:", "Passed" if result2 == output2 else f"Failed (Got {result2})")

# Test case 3:
input3 = "/home/user/Documents/../Pictures"
output3 = "/home/user/Pictures"
result3 = Solution().simplifyPath(input3)
print("Test case 3:", "Passed" if result3 == output3 else f"Failed (Got {result3})")
```
