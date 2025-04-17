# Generate Parentheses
# Stack (backtracking) Solution:
from typing import List
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
    
# Time Complexity: O(4^n / sqrt(n)) which is the number of valid combinations of parentheses.
# Space Complexity: O(n) for the recursion stack and the result list.
# The recursion stack can go up to O(n) depth, and the result list can store up to O(4^n / sqrt(n)) valid combinations.
# This solution is more efficient than the brute force solution because it avoids generating invalid combinations.
# The backtracking approach generates only valid combinations by ensuring that the number of closing parentheses never exceeds the number of opening parentheses at any point in the recursion.

# Test Cases:
# Test Case 1
print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]

# Test Case 2
print(Solution().generateParenthesis(1)) # ["()"]
