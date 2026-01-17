# Final Prices With a Special Discount in a Shop
# Stack Solution:
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [p for p in prices]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]

            stack.append(i)

        return res

# Time Complexity: O(n), where n is the length of the prices array. Each element is pushed and popped from the stack at most once.
# Space Complexity: O(n) in the worst case, where n is the length of the prices array, for the stack and the result array.
# This stack solution is efficient and effectively finds the next lesser or equal price for each item to apply the discount.


# Test Cases:
# Test Case 1:
prices = [8, 4, 6, 2, 3]
print(Solution().finalPrices(prices))  # Expected Output: [4, 2, 4, 2, 3]

# Test Case 2:
prices = [1, 2, 3, 4, 5]
print(Solution().finalPrices(prices))  # Expected Output: [1, 2, 3, 4, 5]

# Test Case 3:
prices = [10, 1, 1, 6]
print(Solution().finalPrices(prices))  # Expected Output: [9, 0, 1, 6]
