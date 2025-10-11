# Minimum Number of Swaps to Make the String Balanced - LeetCode

## Problem Explanation

The **Minimum Number of Swaps to Make the String Balanced** problem involves determining the smallest number of swaps required to make a string of brackets balanced.

You are given an even-length string `s` containing an equal number of opening brackets `'['` and closing brackets `']'`. A string is **balanced** if:

1. It is empty, or
2. It can be written as `AB`, where both `A` and `B` are balanced, or
3. It can be written as `[C]`, where `C` is balanced.

You can swap any two characters in the string any number of times. The goal is to find the minimum number of swaps needed to make the string balanced.

### Example

```text
Input: s = "][]["
Output: 1
Explanation: Swap index 0 with index 3 → "[[]]"
```

---

## Code Explanation with Comments

### Stack-Based Solution

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []  # Stack to track unmatched opening brackets
        for c in s:
            if c == '[':
                stack.append(c)  # Add opening bracket to stack
            elif stack:
                # If current is ']' and stack has an opening '[', remove it (balanced pair)
                stack.pop()
        # The remaining unmatched '[' brackets determine the number of swaps
        return (len(stack) + 1) // 2
```

**Explanation:**

* Traverse through the string.
* Push `'['` into the stack when encountered.
* When `']'` is encountered and the stack is not empty, pop one `'['` (since they form a valid pair).
* After processing all characters, the remaining unmatched `'['` count tells how many swaps are needed.
* Formula `(len(stack) + 1) // 2` calculates the minimum swaps required.

**Time Complexity:** O(n) we process each character once.
**Space Complexity:** O(n) in the worst case, all brackets are unmatched.

---

### Greedy Solution

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        stackSize = 0  # Counter for unmatched '[' brackets
        for c in s:
            if c == '[':
                stackSize += 1  # Increment when encountering '['
            elif stackSize > 0:
                stackSize -= 1  # Decrement when a matching pair is found
        # Remaining unmatched opening brackets determine swaps
        return (stackSize + 1) // 2
```

**Explanation:**

* Instead of using a stack, this version keeps a simple counter.
* Every `'['` increases the counter, and every `']'` decreases it if possible.
* The remaining unmatched `'['` count determines the number of swaps needed.

**Time Complexity:** O(n) one pass through the string.
**Space Complexity:** O(1) only uses a few variables.

---

## Approach and Logic in Simple Terms

Imagine balancing brackets as ensuring that each `'['` has a matching `']'`.

* When brackets are out of order (for example, too many `']'` before `'['`), we must swap to fix it.
* The key observation is that each swap can fix **two** unbalanced positions.

The **stack solution** explicitly tracks unmatched brackets, while the **greedy solution** just counts how many are unmatched — both arrive at the same result.

---

## Differences Between the Two Solutions

| Aspect               | Stack Solution                           | Greedy Solution                            |
| -------------------- | ---------------------------------------- | ------------------------------------------ |
| **Logic**            | Uses an explicit stack to match brackets | Uses a counter to track unmatched brackets |
| **Space Complexity** | O(n)                                     | O(1)                                       |
| **Implementation**   | Easier to visualize for beginners        | More efficient and cleaner                 |
| **Performance**      | Slightly higher memory usage             | Optimal for both time and space            |

---

## Optimal Solution and Reasoning

The **greedy approach** is the most optimal solution:

* It runs in **O(n)** time.
* It uses **O(1)** space.

Since both solutions require only one traversal through the string, time cannot be improved further. The greedy method avoids using extra data structures, making it the best choice for large input sizes.
