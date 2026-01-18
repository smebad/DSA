# Removing Stars From a String - LeetCode

## 1. Problem Explanation

**Removing Stars From a String** is a string manipulation problem where you are given a string `s` consisting of lowercase English letters and the character `*` (star).

Each star represents an operation that removes:

1. The star itself
2. The closest non-star character to its left

You must perform this operation for **all stars** in the string and return the final string after all removals are completed.

### Important Notes

* The input is always valid, meaning there will always be a non-star character available to remove when a star appears.
* The final resulting string is guaranteed to be unique.

### Example

Input:

```
"leet**cod*e"
```

Output:

```
"lecoe"
```

---

## 2. Code With Comments

Below is your provided stack-based solution with detailed comments added for easy revision.

```python
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []  # Stack to keep track of valid characters

        # Traverse each character in the string
        for c in s:
            # If the character is a star, remove the last valid character
            if c == "*":
                # Stack is guaranteed to be non-empty due to problem constraints
                stack.pop()
            else:
                # If it is a normal character, push it onto the stack
                stack.append(c)

        # Join the remaining characters in the stack to form the final string
        return "".join(stack)
```

---

## 3. Solution Approach and Logic

### Key Idea

This problem is best solved using a **stack** because:

* You need to remove the **most recent valid character** when a star appears
* Stack naturally follows a **Last-In-First-Out (LIFO)** order

### Step-by-Step Logic

1. Initialize an empty stack
2. Traverse the string character by character
3. For each character:

   * If it is a normal letter, push it onto the stack
   * If it is `*`, pop the top element from the stack (the closest character to the left)
4. After processing all characters, the stack contains only the remaining valid characters
5. Convert the stack into a string and return it

### Why This Works

Each `*` removes exactly one character before it. Since operations always affect the **most recent character**, a stack perfectly models this behavior.

---

## 5. Time and Space Complexity

### Time Complexity

* **O(n)** where `n` is the length of the string
* Each character is processed once
* Stack push and pop operations take constant time

### Space Complexity

* **O(n)** in the worst case
* This happens when the string contains no stars and all characters are stored in the stack

---

## 6. Why This Is the Most Optimal Solution

* The problem requires checking each character at least once
* Stack ensures minimal operations per character
* No extra passes or string rebuilding

Because of this, **O(n) time with O(n) space** is the most optimal and practical solution for this problem.

---

## 7. Test Cases

```python
# Test Case 1
s1 = "leet**cod*e"
print(Solution().removeStars(s1))  # Output: "lecoe"

# Test Case 2
s2 = "erase*****"
print(Solution().removeStars(s2))  # Output: ""
```