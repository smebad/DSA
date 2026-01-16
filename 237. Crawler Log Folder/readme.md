# Crawler Log Folder - LeetCode

## 1. Problem Explanation

**Crawler Log Folder** is a simulation problem based on navigating a file system using log operations.

You are given a list of folder change operations performed by a user. The system starts in the **main folder**, and each log represents a command that changes the current directory.

Your task is to determine the **minimum number of operations required to return to the main folder** after all the given operations are performed.

### Supported Operations

* `"../"` : Move to the parent folder (if already in the main folder, stay there)
* `"./"` : Stay in the current folder
* `"x/"` : Move into a child folder named `x`

### Goal

After applying all operations in order, return how many `"../"` operations are needed to get back to the main folder.

---

## 2. Code With Comments

Below is your provided solution with detailed comments added to help you remember the logic:

```python
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0  # Tracks the current depth relative to the main folder

        # Iterate through each folder operation
        for log in logs:
            if log == "./":
                # Stay in the same folder, no change in depth
                continue

            if log == "../":
                # Move up one folder, but never go above the main folder
                res = max(0, res - 1)
            else:
                # Move into a child folder, increase depth
                res += 1

        # The depth represents how many steps are needed to return to main folder
        return res
```

---

## 3. Solution Approach and Logic

### Key Idea

Instead of tracking actual folder names, we only need to track **how deep we are** in the directory tree compared to the main folder.

### How the Logic Works

* Start at depth `0` (main folder)
* For each log:

  * `"./"` does nothing
  * `"x/"` increases depth by `1`
  * `"../"` decreases depth by `1`, but never below `0`

At the end, the depth value tells us exactly how many times we must use `"../"` to return to the main folder.

### Why This Works

* We only care about **relative position**, not actual folder names
* Each valid folder move changes depth in a predictable way
* This avoids unnecessary data structures like stacks

---

## 4. Time and Space Complexity

### Time Complexity

* **O(n)** where `n` is the number of log entries
* Each operation is processed exactly once

### Space Complexity

* **O(1)**
* Only a single integer variable is used

### Why This Is the Most Optimal Solution

* No extra memory allocation
* No need to store folder names
* Direct simulation with constant space

This makes the solution both **fast and memory-efficient**, ideal for large inputs.

---

## 5. Example Walkthrough

### Input

```
["d1/","d2/","../","d21/","./"]
```

### Depth Changes

| Operation | Depth |
| --------- | ----- |
| d1/       | 1     |
| d2/       | 2     |
| ../       | 1     |
| d21/      | 2     |
| ./        | 2     |

Final depth = `2` → Need `2` operations to return to main folder

---

## 6. Test Cases:
```python
solution = Solution()
print(solution.minOperations(["d1/","d2/","../","d21/","./"]))  # Output: 2
print(solution.minOperations(["d1/","d2/","./","d3/","../","d31/"]))  # Output: 3
print(solution.minOperations(["d1/","../","../","../"]))  # Output: 0
```