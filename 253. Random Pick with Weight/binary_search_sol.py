# Random Pick with Weight
# Binary Search Solution:
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for wgt in w:
            self.prefix.append(self.prefix[-1] + wgt)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        l, r = 1, len(self.prefix)
        while l < r:
            mid = (l + r) >> 1
            if self.prefix[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l - 1

# Time Complexity: O(n), where n is the length of the input list w. This is due to the construction of the prefix sum array in the __init__ method.
# Space Complexity: O(n), where n is the length of the input list w.
# This solution is efficient for multiple calls to pickIndex() after the initial setup, as each call to pickIndex() runs in O(log n) time due to the binary search.



# Test Cases
# Test Case 1:
solution = Solution([1])
print(solution.pickIndex())  # Expected output: 0

# Test Case 2:
solution = Solution([1, 3])
print(solution.pickIndex())  # Expected output: 1
