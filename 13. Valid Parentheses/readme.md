# Valid Parentheses - LeetCode DSA Problem

## Problem Description
The **Valid Parentheses** problem is a common data structures and algorithms (DSA) challenge where you are given a string `s` consisting of characters: `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`. The task is to determine whether the input string is valid.

A string is considered valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every closing bracket has a corresponding opening bracket of the same type.

### Example Inputs and Outputs
- Input: `"()"`  
  Output: `true`

- Input: `"()[]{}"`  
  Output: `true`

- Input: `"(]"`  
  Output: `false`

- Input: `"([])"`  
  Output: `true`

### Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

---

## Solutions

### Brute Force Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
```
#### Explanation:
- The solution repeatedly removes valid pairs of brackets (`()`, `{}`, `[]`) from the string.
- The loop continues until no more pairs can be removed.
- If the string becomes empty by the end, it means all brackets were properly matched and nested.

#### Time Complexity:
- **O(n^2)**: Each `replace` operation takes O(n) and we could perform it up to n times.

#### Space Complexity:
- **O(n)**: Due to repeated creation of new strings during replacement operations.

#### Notes:
- This approach is simple but inefficient for large strings.

---

### Stack-Based Optimal Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
```

#### Explanation:
- A stack is used to keep track of the opening brackets.
- For every closing bracket, the code checks whether it matches the top of the stack.
- If it does, pop it; otherwise, return `False`.
- At the end, the stack should be empty for the input to be valid.

#### Time Complexity:
- **O(n)**: We process each character exactly once.

#### Space Complexity:
- **O(n)**: In the worst case, we might store all opening brackets in the stack.

#### Notes:
- This is the optimal solution in terms of time and space efficiency for this problem.
- Stack based matching is a classic and scalable way to validate nested structures.

---

## Conclusion
The **Valid Parentheses** problem is an excellent example of using stacks to solve problems involving balanced expressions. While the brute force method works for small strings, the stack-based approach is the most efficient and scalable solution for large input sizes.