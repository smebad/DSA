# Generate Parentheses - LeetCode Problem

## Problem Statement
Given `n` pairs of parentheses, write a function to generate all combinations of well formed parentheses.

### Examples
**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

### Constraints
```
1 <= n <= 8
```

---

## What is "Generate Parentheses"?
This is a classic problem in data structures and algorithms (DSA) that involves generating all possible strings of well formed (balanced) parentheses using `n` pairs. A well formed parentheses string ensures that for every opening bracket `(` there exists a closing bracket `)` placed in the correct order.

This problem is typically solved using recursion and backtracking. It is a great example of exploring the full possibility space with constraints applied to reduce unnecessary computations.

---

## Brute Force Solution
### Code Overview
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return res
```

### Explanation
- `dfs(s)`: This recursive function generates all strings of length `2 * n` using only `(` and `)`.
- `valid(s)`: Checks if the generated string is valid (balanced parentheses).
- If the generated string has the correct length and is valid, it's added to the result list `res`.

### Time and Space Complexity
- **Time Complexity:** `O(2^(2n) * n)` or `O(2^n * n)` because we generate all possible combinations and validate each in `O(n)`.
- **Space Complexity:** `O(2^n * n)` for storing the result list. The recursion stack goes up to `O(n)` depth.

---

## Optimal Solution (Backtracking)
### Code Overview
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
```

### Explanation
- This uses a **backtracking** approach to build the solution.
- At each recursion level, we can:
  - Add an opening parenthesis `(` if we still have unused ones.
  - Add a closing parenthesis `)` only if it won’t break the balance.
- The combination is added to the result list `res` when both open and close counts reach `n`.

### Time and Space Complexity
- **Time Complexity:** `O(4^n / sqrt(n))`, which is the nth Catalan number. This is the number of valid sequences.
- **Space Complexity:** `O(n)` for the recursion stack. The result list stores all valid combinations.

### Why is this optimal?
- It prunes invalid combinations early and avoids extra validation logic.
- It ensures valid sequences only, reducing the search space significantly compared to the brute force method.

---

## Conclusion
The backtracking approach is the most optimal solution for this problem. It eliminates the overhead of generating and then validating strings by ensuring the validity at the time of construction. This leads to efficient execution both in terms of time and space.

