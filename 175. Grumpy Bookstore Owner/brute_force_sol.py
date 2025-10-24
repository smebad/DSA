# Grumpy Bookstore Owner
# Brute Force Solution:
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res, n = 0, len(customers)
        for i in range(n):
            if not grumpy[i]:
                res += customers[i]

        satisfied = res
        for i in range(n - minutes + 1):
            cur = 0
            for j in range(i, i + minutes):
                if grumpy[j]:
                    cur += customers[j]
            res = max(res, satisfied + cur)

        return res
    
# Time Complexity: O(n * m), where n is the length of the customers array and m is the value of minutes. This is due to the two nested loops, one for the outer loop and one for the inner loop.
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
# This brute force solution may not be efficient for large inputs due to its O(n * m) time complexity. However, it correctly implements the logic to find the maximum number of satisfied customers by checking all possible intervals of length minutes.


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
