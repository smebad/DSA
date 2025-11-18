# K-th Symbol in Grammar - LeetCode

## 1. Problem Explanation: What is "K-th Symbol in Grammar"?

The problem describes a special sequence of binary strings that grows row by row based on a simple rule.

* Start with row 1: `0`
* To form the next row:

  * Replace every `0` with `01`
  * Replace every `1` with `10`

Examples:

* Row 1: `0`
* Row 2: `01`
* Row 3: `0110`
* Row 4: `01101001`

Given two values **n** and **k**, the task is to return the **k-th symbol in the n-th row**.

A key detail is that **n and k are 1-indexed**, meaning counting starts from 1.

The main challenge is that the string grows exponentially. The n-th row has length `2^(n-1)`, so generating full rows is not efficient. Instead, we need a mathematical or logical approach to directly find the k-th symbol.

---

## 2. Code Explanation With Comments

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0  # Start with row 1 which is always '0'
        left, right = 1, 2 ** (n - 1)  # The range of positions in row n

        for _ in range(n - 1):  # We will go row by row until reaching row n
            mid = (left + right) // 2  # Midpoint divides the row into left and right halves

            if k <= mid:
                # If k is in the left half, the symbol stays the same
                right = mid
            else:
                # If k is in the right half, flip the current symbol
                left = mid + 1
                cur = 0 if cur else 1  # Flip: 0 -> 1, 1 -> 0

        return cur
```

### What the code does in simple words

* Instead of building long rows, we track **whether the current position is in the left or right half of the row**.
* Every time `k` falls in the right half, we flip the symbol.
* The number of flips determines whether the symbol ends as `0` or `1`.

---

## 3. Approach and Logic

### Key idea

Each row is formed from the previous one. The left half always copies the previous row directly. The right half is the flipped version of the previous row.

This leads to an important observation:

* If k is in the **left half**, the symbol is the same as in the previous row.
* If k is in the **right half**, the symbol is the **opposite** of the symbol in the previous row.

### Example

Row 3 is `0110`.
Positions:
1 2 3 4
L L R R

If we want the 3rd symbol:

* It is in the right half
* So it will be a flipped version of row 2's symbol at position k - mid

### Why flipping works

`0` produces `01`
`1` produces `10`

Left half = same
Right half = flipped

---

## 4. Time and Space Complexity

### Time Complexity: **O(n)**

* We reduce the search range row by row until reaching row n.
* We perform a constant amount of work in each step.
* Total steps = n - 1.

Since n ≤ 30, this is extremely fast.

### Space Complexity: **O(1)**

* Only a few primitive variables are used.
* No recursion, no extra arrays or strings.

### Why this is the most optimal solution

* Generating full rows would require `O(2^n)` time and space, which is impossible for large n.
* Recursion adds `O(n)` space for the call stack.
* The provided iterative method uses only logic and math, avoiding all overhead.

---

## 5. Test Cases
```python
sol = Solution()

# Test Case 1:
n = 1
k = 1
print(sol.kthGrammar(n, k))  # Output: 0

# Test Case 2:
n = 2
k = 1
print(sol.kthGrammar(n, k))  # Output: 0

# Test Case 3:
n = 2
k = 2
print(sol.kthGrammar(n, k))  # Output: 1
```