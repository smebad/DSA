# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# Brute Force Solution:
from typing import List
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
    
# Time Complexity: O(2^2n * n) which means O(2^n * n) because we have 2^n possible strings of length 2n and we check each string for validity in O(n) time.
# Space Complexity: O(2^2n * n) which means O(2^n * n) because we have 2^n possible strings of length 2n and we store them in the result list.
# The recursion stack can go up to O(n) depth, but the main space complexity comes from the result list.

# Test Cases:
# Test Case 1
print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]

# Test Case 2
print(Solution().generateParenthesis(1)) # ["()"]