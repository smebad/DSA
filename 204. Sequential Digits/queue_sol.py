# Sequential Digits
# Queue-Based Solution:
from typing import List
from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 10))

        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                queue.append(n * 10 + (ones + 1))

        return res

# Time Complexity: O(1), since there are a fixed number of sequential digit numbers (36) within the given constraints.
# Space Complexity: O(1), as the queue will hold a limited number of elements at any time.
# This queue-based solution efficiently generates sequential digit numbers without checking each number in the range, making it more optimal than the brute force approach.

# Test Cases
sol = Solution()

# Test Case 1:
low1 = 100
high1 = 300
print(sol.sequentialDigits(low1, high1))  # Output: [123, 234]

# Test Case 2:
low2 = 1000
high2 = 13000
print(sol.sequentialDigits(low2, high2))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]
