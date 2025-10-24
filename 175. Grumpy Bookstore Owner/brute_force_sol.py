# Grumpy Bookstore Owner
# There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

# During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

# Return the maximum number of customers that can be satisfied throughout the day.

 

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

# Output: 16

# Explanation:

# The bookstore owner keeps themselves not grumpy for the last 3 minutes.

# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1

# Output: 1

 

# Constraints:

# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 104
# 0 <= customers[i] <= 1000
# grumpy[i] is either 0 or 1.


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