# Baseball Game
# Stack-based solution:

from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
    
# Time Complexity: O(n), where n is the number of operations. This is because we iterate through the operations list once, and each operation takes constant time to process.
# Space Complexity: O(n), where n is the number of operations. In the worst case, we may store all operations in the stack if none are invalidated.
# This solution is efficient and straightforward, leveraging the stack data structure to keep track of scores and apply the game rules as specified.


# Test Cases
# Test Case 1:
ops = ["5", "2", "C", "D", "+"]
solution = Solution()
result = solution.calPoints(ops)
print(result)  # Output: 30

# Test Case 2:
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
solution = Solution()
result = solution.calPoints(ops)
print(result)  # Output: 27

# Test Case 3:
ops = ["1", "C"]
solution = Solution()
result = solution.calPoints(ops)
print(result)  # Output: 0
