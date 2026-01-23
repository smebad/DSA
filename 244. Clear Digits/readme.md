# Clear Digits - LeetCode

## 1. Problem Explanation

You are given a string `s` that contains lowercase letters and digits. The goal is to remove all digits using a special rule:

Every time you see a digit, you must remove that digit and also remove the closest non-digit character to its left. This operation is repeated until all digits are removed. The problem guarantees that every digit will always have a non-digit character to its left, so the operation is always possible.

The task is to return the final string after all digits have been removed.

---

## 2. Code with Comments

```python
class Solution:
    def clearDigits(self, s: str) -> str:
        res = []  # This acts like a stack to store valid characters

        # Custom function to check if a character is a digit
        def isdigit(c):
            return ord("0") <= ord(c) <= ord("9")
        
        for i in range(len(s)):
            # If current character is a digit, remove the last non-digit
            if isdigit(s[i]):
                res.pop()
            else:
                # If it is a letter, store it
                res.append(s[i])

        # Convert stack back to string
        return "".join(res)
```

---

## 3. Approach and Logic

This problem is best solved using a stack-based approach.

We scan the string from left to right:

* If we see a letter, we push it into the stack.
* If we see a digit, we remove the last letter from the stack, because that is the closest non-digit character to the left.

By doing this, we are directly simulating the rules of the problem in a simple and efficient way.

### Why a Stack Works

A stack always keeps track of the most recent characters. When a digit appears, the character that must be deleted is always the most recently added non-digit character, which is exactly what a stack gives us.

There are no alternative efficient solutions needed for this problem because the stack approach naturally fits the problem rules.

---

## 4. Time and Space Complexity

### Time Complexity

O(n), where n is the length of the string. Each character is processed once.

### Space Complexity

O(n) in the worst case, when the string contains no digits and all characters are stored in the stack.

### Why This Is Optimal

This solution is optimal because:

* It processes each character only once.
* It uses only a single stack for tracking characters.
* No unnecessary extra data structures or repeated scans are used.

---

## Test Cases:
```python
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "abc"
    print(solution.clearDigits(s1))  # Expected Output: "abc"

    # Test Case 2
    s2 = "cb34"
    print(solution.clearDigits(s2))  # Expected Output: ""
```