# K-th Symbol in Grammar
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
