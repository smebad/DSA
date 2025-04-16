# Evaluate Reverse Polish Notation

# Stack solution:
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
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
    
# Time complexity: O(n), where n is the number of tokens.
# Space complexity: O(n), where n is the number of tokens.


# Test Cases:
# Test Case 1
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens)) # 9

# Test Case 2
tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens)) # 6

# Test Case 3
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens)) # 22
