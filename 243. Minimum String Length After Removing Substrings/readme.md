# Minimum String Length After Removing Substrings - LeetCode

## 1. Problem Explanation

You are given a string `s` consisting only of uppercase English letters. You are allowed to repeatedly remove any occurrence of the substrings "AB" or "CD" from the string. After each removal, the remaining parts of the string join together, which can form new "AB" or "CD" patterns that can also be removed.

Your task is to return the minimum possible length of the string after performing all possible valid removals.

The key challenge is that removing one pair can create a new removable pair across the boundary, so the order of removals matters. We need a method that always leads to the smallest possible final string.

---

## 2. Code With Comments

```python
class Solution:
    def minLength(self, s: str) -> int:
        stack = []  # This stack will store the characters that are not yet removed

        for c in s:
            # Add the current character to the stack
            stack.append(c)
            
            # Check if the top two characters of the stack form "AB" or "CD"
            if (len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B") or
                (stack[-2] == "C" and stack[-1] == "D")
            )):
                # If they form a removable substring, remove both characters
                stack.pop()
                stack.pop()

        # The stack now contains only the remaining characters
        return len(stack)
```

---

## 3. Solution Approach and Logic

### Core Idea

We use a stack to simulate building the string while removing "AB" and "CD" whenever they appear.

We go through the string character by character:

* Add each character to a stack.
* After adding, check the top two characters of the stack.
* If they form "AB" or "CD", remove them immediately.

This works because:

* A stack naturally keeps track of the most recent characters.
* If removing a pair creates a new pair, it will appear at the top of the stack and be removed automatically.

This mimics how the string would shrink and reconnect in real operations.

### Why this greedy method works

Whenever "AB" or "CD" appears, it is always beneficial to remove it immediately. Waiting does not give a better result because removing it later or now leads to the same or larger remaining string. Removing early also allows new pairs to form.

---

## 4. Time and Space Complexity

### Time Complexity

O(n)

We iterate through the string once. Each character is pushed onto the stack at most once and popped at most once.

### Space Complexity

O(n)

In the worst case, no characters can be removed, so all characters remain in the stack.

---

## 5. Why This Is the Most Optimal Solution

This stack-based solution is optimal because:

* It processes each character only once.
* It removes pairs immediately when they appear.
* It avoids repeated scanning or rebuilding of the string.

---

## 6. Test Cases
```python
# Test Case 1:
s1 = "ABFCACDB"
sol = Solution()
print(sol.minLength(s1))  # Expected output: 2

# Test Case 2:  
s2 = "ACBBD"
print(sol.minLength(s2))  # Expected output: 5
```