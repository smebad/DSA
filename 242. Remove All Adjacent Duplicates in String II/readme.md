# Remove All Adjacent Duplicates in String II - LeetCode

## 1. Problem Explanation

You are given a string `s` and an integer `k`. A `k` duplicate removal means removing `k` adjacent identical characters from the string. After removal, the left and right parts of the string join together, which may create new groups of adjacent duplicates. This process continues until no more groups of `k` identical adjacent characters remain.

The goal is to return the final string after all possible removals.

Example:

```
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
```

Because:

* Remove "eee" and "ccc" → "ddbbbdaa"
* Remove "bbb" → "dddaa"
* Remove "ddd" → "aa"

---

## 2. Code With Comments

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack will store pairs of [character, count]
        stack = []

        # Traverse each character in the string
        for c in s:
            # If the stack is not empty and the current character
            # is the same as the last one in the stack
            if stack and stack[-1][0] == c:
                # Increase the count of the last character
                stack[-1][1] += 1
            else:
                # Otherwise, push the new character with count 1
                stack.append([c, 1])

            # If the count reaches k, remove that group
            if stack[-1][1] == k:
                stack.pop()

        # Rebuild the final string from the stack
        return ''.join(char * count for char, count in stack)
```

---

## 3. Approach and Logic Explained

This problem is best solved using a stack because we need to track consecutive characters and how many times they appear in a row.

### How the algorithm works:

1. We scan the string from left to right.
2. For each character:

   * If it is the same as the character on top of the stack, we increase its count.
   * Otherwise, we push a new entry with count 1.
3. Whenever the count becomes equal to `k`, we remove that entry from the stack.
4. At the end, we build the result by repeating each character according to its count.

This works because the stack always represents the current state of the string after all valid removals so far.

### Why this approach is effective

Removing characters in the middle of a string is expensive. The stack allows us to simulate this efficiently without repeatedly modifying the string.

---

## 4. Time and Space Complexity

### Time Complexity: O(n)

We process each character once. Each character is added and removed from the stack at most once, so the total work is linear.

### Space Complexity: O(n)

In the worst case, no characters are removed, so all characters are stored in the stack.

### Why this is optimal

Any solution must look at every character at least once, so O(n) time is the best possible. The stack-based method achieves this while keeping the implementation simple and efficient.

---

## 5. Example Walkthrough

For `s = "deeedbbcccbdaa"` and `k = 3`:

| Step | Stack State               |
| ---- | ------------------------- |
| d    | [(d,1)]                   |
| e    | [(d,1),(e,1)]             |
| e    | [(d,1),(e,2)]             |
| e    | [(d,1)] removed (e,3)     |
| d    | [(d,2)]                   |
| b    | [(d,2),(b,1)]             |
| b    | [(d,2),(b,2)]             |
| b    | [(d,2)] removed (b,3)     |
| c    | [(d,2),(c,1)]             |
| c    | [(d,2),(c,2)]             |
| c    | [(d,2)] removed (c,3)     |
| b    | [(d,2),(b,1)]             |
| d    | [(d,2),(b,1),(d,1)]       |
| a    | [(d,2),(b,1),(d,1),(a,1)] |
| a    | [(d,2),(b,1),(d,1),(a,2)] |

Then the chain reactions remove remaining groups until only "aa" remains.

---

## 6. Test Cases
```python
# Test Case 1
print(Solution().removeDuplicates('abcd', 2)) # 'abcd'

# Test Case 2
print(Solution().removeDuplicates('deeedbbcccbdaa', 3)) # 'aa'

# Test Case 3
print(Solution().removeDuplicates('pbbcggttciiippooaais', 2)) # 'ps'
```