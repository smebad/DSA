# Validate Stack Sequences
# Stack Solution:
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack

# Time Complexity: O(n), where n is the length of the pushed array. Each element is pushed and popped at most once.
# Space Complexity: O(n) in the worst case, where all elements are pushed onto the stack without any pops.
# This stack solution is efficient and straightforward, simulating the push and pop operations to validate the sequences.


# Test Cases:

# Test Case 1:
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(Solution().validateStackSequences(pushed, popped))  # Expected Output: True

# Test Case 2:
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(Solution().validateStackSequences(pushed, popped))  # Expected Output: False

# Test Case 3:
pushed = [2, 1, 0]
popped = [1, 2, 0]
print(Solution().validateStackSequences(pushed, popped))  # Expected Output: True
