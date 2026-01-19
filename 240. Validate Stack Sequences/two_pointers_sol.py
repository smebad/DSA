# Validate Stack Sequences
# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
 

# Constraints:

# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.


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