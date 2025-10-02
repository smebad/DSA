# Average Waiting Time
# Simulation Solution:
from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        total = 0

        for arrival, order in customers:
            if time > arrival:
                total += time - arrival
            else:
                time = arrival
            total += order
            time += order

        return total / len(customers)
    
# Time Complexity: O(n), where n is the number of customers. We iterate through the list of customers once.
# Space Complexity: O(1), we use a constant amount of space regardless of the input size.
# This solution efficiently calculates the average waiting time by simulating the chef's workflow and keeping track of the total waiting time and the current time.


# Test Cases:
solution = Solution()

# Test Case 1:
customers1 = [[1,2],[2,5],[4,3]]
print(solution.averageWaitingTime(customers1))  # Expected output: 5.0

# Test Case 2:
customers2 = [[5,2],[5,4],[10,3],[20,1]]

print(solution.averageWaitingTime(customers2))  # Expected output: 3.25
