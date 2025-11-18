# K-th Symbol in Grammar
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01
# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation: 
# row 1: 0
# row 2: 01
 

# Constraints:

# 1 <= n <= 30
# 1 <= k <= 2n - 1

# Iteration Solution:
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        left, right = 1, 2 ** (n - 1)

        for _ in range(n - 1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                cur = 0 if cur else 1

        return cur
    
# Time Complexity: O(n), where n is the number of rows. We iterate through each row once.
# Space Complexity: O(1), we use a constant amount of space.
# This solution iteratively determines the k-th symbol in the n-th row by tracking the current symbol and adjusting the search range based on the position of k relative to the midpoint of the current row. So this approach avoids the overhead of recursion and uses constant space.


# Test Cases
sol = Solution()

# Test Case 1:
n = 1
k = 1
print(sol.kthGrammar(n, k))  # Output: 0

# Test Case 2:
n = 2
k = 1
print(sol.kthGrammar(n, k))  # Output: 0

# Test Case 3:
n = 2
k = 2
print(sol.kthGrammar(n, k))  # Output: 1