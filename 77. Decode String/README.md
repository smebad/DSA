# Decode String - LeetCode

## Problem Description

The **Decode String** problem requires decoding an encoded string where the encoding format is defined as:

```
k[encoded_string]
```

Here, `k` is a positive integer and `encoded_string` is repeated exactly `k` times. The input is always valid and contains only lowercase English letters, digits (for repetition count), and square brackets.

### Examples

* Input: `"3[a]2[bc]"`  → Output: `"aaabcbc"`
* Input: `"3[a2[c]]"`  → Output: `"accaccacc"`
* Input: `"2[abc]3[cd]ef"`  → Output: `"abcabccdcdcdef"`

### Constraints

* 1 <= s.length <= 30
* s consists of lowercase letters, digits, and brackets
* All integers k are in the range \[1, 300]

---

## One Stack Solution

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # Extract substring within brackets
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()  # Remove the opening bracket '['

                # Extract repeat count (k)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # Repeat the substring and push back to stack
                stack.append(int(k) * substr)

        return "".join(stack)
```

---

## Explanation of Code

* We iterate through each character in the string.
* Characters are pushed onto a stack until we encounter a closing bracket `]`.
* On encountering `]`, we pop elements from the stack until we reach `[` to extract the substring.
* After removing `[`, we pop the digits to form the repeat count `k`.
* We repeat the substring `k` times and push it back onto the stack.
* Finally, we join all stack elements to form the decoded string.

---

## Approach and Logic

* The approach uses a **stack** to simulate the nested structure of encoded strings.
* It allows easy backtracking from `]` to the corresponding `[` and building the repeated substring.
* This method efficiently handles multiple levels of nesting like `3[a2[c]]`.

### Why It Works

* The stack ensures that deeply nested encodings are decoded from the innermost level outward.
* Repetition is handled by converting digits to integers and repeating the string accordingly.

---

## Time and Space Complexities

* **Time Complexity:** `O(n + N^2)`

  * `O(n)` for iterating through the input string.
  * `O(N^2)` can occur due to string concatenation during substring repetition.

* **Space Complexity:** `O(n + N^2)`

  * Stack can grow up to the input size `n`.
  * Final output string could grow up to `N^2` in the worst case.

### Optimality

* For the given constraints (max length 30), this solution is very efficient.
* It balances readability and performance, and handles all cases correctly using one stack.

---

## Test Cases

```python
# Test Case 1:
s1 = "3[a]2[bc]"
print(Solution().decodeString(s1))  # Output: "aaabcbc"

# Test Case 2:
s2 = "3[a2[c]]"
print(Solution().decodeString(s2))  # Output: "accaccacc"

# Test Case 3:
s3 = "2[abc]3[cd]ef"
print(Solution().decodeString(s3))  # Output: "abcabccdcdcdef"
```
