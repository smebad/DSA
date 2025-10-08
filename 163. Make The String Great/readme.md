# Make The String Great - LeetCode

## Problem Explanation

The **Make The String Great** problem asks us to remove pairs of adjacent characters in a string that differ only in case (one is uppercase and the other is lowercase of the same letter). We repeat this process until no such adjacent pairs remain. The resulting string is called a *good string*.

### Problem Definition

You are given a string `s` consisting of lowercase and uppercase English letters. A *good string* does not have two adjacent characters `s[i]` and `s[i + 1]` where one is the same letter in the opposite case.

You can repeatedly remove any two such adjacent characters until the string becomes good. The final good string is guaranteed to be unique.

**Example 1:**

```
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: Removing either 'eE' or 'Ee' makes the string good.
```

**Example 2:**

```
Input: s = "abBAcC"
Output: ""
Explanation: All pairs can be removed step by step until the string is empty.
```

**Example 3:**

```
Input: s = "s"
Output: "s"
Explanation: A single character is already a good string.
```

---

## Two-Pointer Solution (In-place Approach)

```python
class Solution:
    def makeGood(self, s: str) -> str:
        l = 0  # acts as a write pointer
        s = list(s)  # convert string to list for in-place modification
        for r in range(len(s)):  # r is the read pointer
            # Check if the current and previous characters differ by 32 (ASCII difference between upper and lower case)
            if l > 0 and abs(ord(s[r]) - ord(s[l - 1])) == 32:
                l -= 1  # remove the previous character if they cancel each other
            else:
                s[l] = s[r]  # keep the current character
                l += 1  # move the write pointer forward
        return ''.join(s[:l])  # rebuild the good string from valid characters
```

### Explanation

* We use **two pointers** (`l` and `r`) to modify the string in place.
* The `r` pointer scans through the string, while `l` represents the position where the next valid character should go.
* If the current character `s[r]` and the previous one `s[l-1]` differ by 32 in ASCII (like `'a'` and `'A'`), we remove the last kept character by moving `l` back.
* Otherwise, we keep the current character.
* At the end, the substring `s[:l]` contains the good string.

### Complexity

* **Time Complexity:** O(n) — We iterate over the string once.
* **Space Complexity:** O(n) — Due to list conversion, but the algorithm modifies the list in place, so extra memory usage is constant beyond that.

This solution is **efficient** because it minimizes space usage by working directly within the list instead of using a stack.

---

## Stack Solution

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # use a stack to store valid characters
        for i in range(len(s)):
            # if current and top of stack differ by 32, they cancel each other
            if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()  # remove the previous character
            else:
                stack.append(s[i])  # keep the current character
        return "".join(stack)  # combine remaining characters into a good string
```

### Explanation

* We use a **stack** to keep track of valid characters.
* For every character in the string:

  * If the stack is not empty and the current character cancels out with the top of the stack (same letter, opposite case), pop the top.
  * Otherwise, push the character onto the stack.
* At the end, joining the stack gives the final good string.

### Complexity

* **Time Complexity:** O(n) — We process each character once.
* **Space Complexity:** O(n) — In the worst case, no pairs cancel out, so all characters stay in the stack.

---

## Comparison Between the Two Solutions

| Aspect                    | Two-Pointer Solution                               | Stack Solution                                  |
| ------------------------- | -------------------------------------------------- | ----------------------------------------------- |
| **Approach**              | Uses two pointers and modifies the string in place | Uses an explicit stack to keep valid characters |
| **Space Complexity**      | O(1) extra (in-place)                              | O(n) in the worst case                          |
| **Ease of Understanding** | Slightly tricky for beginners                      | More intuitive (stack pop/push)                 |
| **Efficiency**            | More space-efficient                               | Easier to read and debug                        |

---

## Optimal Solution

The **two-pointer solution** is the most optimal one because:

* It performs all operations in **O(n)** time.
* It uses only **constant extra space** (excluding the list conversion, which is necessary for mutability in Python).
* It avoids using an auxiliary stack, which reduces memory overhead.

Thus, the two-pointer solution is both **time-optimal and space-optimal** for this problem.