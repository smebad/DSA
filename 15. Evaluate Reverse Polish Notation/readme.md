# Evaluate Reverse Polish Notation - LeetCode

## Problem Description

Evaluate Reverse Polish Notation (RPN) is a classic stack based problem that appears in technical interviews and coding assessments. You are given an array of strings `tokens` representing an arithmetic expression in Reverse Polish Notation.

In Reverse Polish Notation, the operator follows its operands. For example, to express `3 + 4`, the RPN expression is `"3 4 +"`.

Your task is to evaluate the expression and return the resulting integer.

### Valid operations:
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/` (integer division, truncate toward zero)

### Assumptions:
- Each operand is an integer or another expression.
- Division between two integers always truncates toward zero.
- No division by zero will occur.
- All expressions are valid.
- Intermediate results fit in a 32-bit signed integer.

## Example Inputs and Outputs

### Example 1:
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2:
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3:
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
```

## Constraints
- 1 <= tokens.length <= 10^4
- tokens[i] is an integer in the range [-200, 200] or one of the four operators

## Python Solution Using Stack

### Code:
```python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  # Truncates toward zero
            else:
                stack.append(int(c))
        return stack[0]
```

## Explanation
This solution uses a **stack**, a last-in-first-out (LIFO) data structure, to evaluate the Reverse Polish Notation expression.

### Step-by-Step Process:
1. Initialize an empty stack.
2. Iterate over each token in the input list.
3. If the token is a number, convert it to an integer and push it onto the stack.
4. If the token is an operator, pop the last two elements from the stack:
   - Perform the operation.
   - Push the result back onto the stack.
   - Note: For subtraction and division, order matters, so you store `a = stack.pop()` and `b = stack.pop()`, then do `b - a` or `b / a`.
5. After processing all tokens, the result is the only element remaining on the stack.

## Time and Space Complexity
- **Time Complexity**: O(n), where `n` is the number of tokens. Each token is processed once.
- **Space Complexity**: O(n), for the stack that stores intermediate values.

## Why This Solution is Optimal
This is the most optimal solution because it ensures:
- Constant time for each arithmetic operation.
- Single pass through the input.
- Minimal memory usage beyond storing intermediate values in the stack.

## Test Cases
```python
# Test Case 1
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))  # Output: 9

# Test Case 2
tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens))  # Output: 6

# Test Case 3
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))  # Output: 22
```

## Summary
This problem teaches how to utilize the stack data structure to evaluate expressions in postfix notation. The solution achieves optimal performance and demonstrates a clean application of stack principles for parsing arithmetic expressions.

