# Grumpy Bookstore Owner
# Sliding Window Solution:
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        window = max_window = 0
        satisfied = 0

        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]

            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1

            max_window = max(window, max_window)

        return satisfied + max_window
        
# Time Complexity: O(n), where n is the length of the customers array. We traverse the array once using the sliding window technique.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This sliding window solution is more efficient than the brute force solution due to its O(n) time complexity.

# Test Cases:
solution = Solution()

# Test Case 1
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(solution.maxSatisfied(customers, grumpy, minutes))  # Expected output: 16

# Test Case 2
customers = [1]
grumpy = [0]
minutes = 1
print(solution.maxSatisfied(customers, grumpy, minutes))  # Expected output: 1
