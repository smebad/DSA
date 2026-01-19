# Validate Stack Sequences
# Two Pointers Solution:
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = r = 0
        for num in pushed:
            pushed[l] = num
            l += 1
            while l > 0 and pushed[l - 1] == popped[r]:
                r += 1
                l -= 1
        return l == 0

# Time Complexity: O(n), where n is the length of the pushed array. Each element is processed at most twice.
# Space Complexity: O(1), as we are using the pushed array itself to simulate the stack, thus not requiring additional space proportional to the input size.
# This two-pointer solution is efficient and uses constant space by reusing the input array to simulate   

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
