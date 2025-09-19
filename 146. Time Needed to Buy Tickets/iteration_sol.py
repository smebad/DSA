# Time Needed to Buy Tickets
# Iteration Solution:
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0

        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)

        return res
    
# Time Complexity: O(n), where n is the length of the tickets array. We iterate through the array once to calculate the total time.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This iterative approach efficiently calculates the total time needed for the person at position k to buy all their tickets by considering the contributions of each person in the queue.

# Test Cases:
sol = Solution()

# Test Case 1:
tickets = [2, 3, 2]
k = 2
print(sol.timeRequiredToBuy(tickets, k))  # Output: 6

# Test Case 2:
tickets = [5, 1, 1, 1]
k = 0
print(sol.timeRequiredToBuy(tickets, k))  # Output: 8