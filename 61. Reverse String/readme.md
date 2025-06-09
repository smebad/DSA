# Reverse String - LeetCode

## Problem Description

The **Reverse String** problem asks us to reverse a string in-place. The input is provided as an array of characters `s`, and we are required to modify the array directly without returning a new one. We must accomplish this using O(1) extra memory.

### Example 1:

* Input: `s = ["h","e","l","l","o"]`
* Output: `s = ["o","l","l","e","h"]`

### Example 2:

* Input: `s = ["H","a","n","n","a","h"]`
* Output: `s = ["h","a","n","n","a","H"]`

### Constraints:

* `1 <= s.length <= 10^5`
* `s[i]` is a printable ASCII character.

---

## Code Explanation

### Two Pointers Solution

```python
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1  # Initialize two pointers at the start and end
        while l < r:
            s[l], s[r] = s[r], s[l]  # Swap characters at l and r
            l += 1  # Move left pointer to the right
            r -= 1  # Move right pointer to the left
```

### Stack Solution

```python
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)  # Push all characters to the stack
        i = 0
        while stack:
            s[i] = stack.pop()  # Pop characters to reverse order
            i += 1
```

### Recursion Solution

```python
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            if l < r:
                reverse(l + 1, r - 1)  # Recursive call
                s[l], s[r] = s[r], s[l]  # Swap elements after recursion
        reverse(0, len(s) - 1)
```

---

## Approach & Logic

### Two Pointers

This method uses two pointers: one starting from the beginning of the list and one from the end. We keep swapping the elements at these two pointers and then move them towards each other until they meet in the middle.

* **Efficient**: Does not require extra memory.
* **Simple to implement**.

### Stack

This solution uses a stack (last-in-first-out) to reverse the string. We first push all characters into the stack and then pop them back into the list.

* **Intuitive for understanding reverse logic**.
* **Uses extra space proportional to the input size**.

### Recursion

This method uses a recursive function that keeps calling itself, narrowing in from the ends of the array. Once the base condition is met, it swaps characters as it unwinds the recursion.

* **Elegant and clean**.
* **Uses extra space due to call stack**.

---

## Time and Space Complexity

| Method       | Time Complexity | Space Complexity | Explanation                                       |
| ------------ | --------------- | ---------------- | ------------------------------------------------- |
| Two Pointers | O(n)            | O(1)             | Iterates through half the list, swaps in-place    |
| Stack        | O(n)            | O(n)             | Uses a stack to temporarily store elements        |
| Recursion    | O(n)            | O(n)             | Recursive calls use the call stack up to n levels |

### Most Optimal Solution

**Two Pointers** is the most optimal solution. It only uses constant extra memory (O(1)) and performs the reversal in a single pass through half the list, making it both space and time efficient.

---

## Test Cases

### Test Case 1

```python
s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)  # Expected: ["o","l","l","e","h"]
```

### Test Case 2

```python
s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
print(s)  # Expected: ["h","a","n","n","a","H"]
```
