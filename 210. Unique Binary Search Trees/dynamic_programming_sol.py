# Unique Binary Search Trees
# Dynamic Programming Solution:
class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total

        return numTree[n]

# Time Complexity: O(n^2), where n is the input integer. We have a nested loop where for each number of nodes, we iterate through all possible roots.
# Space Complexity: O(n), as we use an array of size n+1 to store the number of unique BSTs for each count of nodes.
# This dynamic programming solution efficiently computes the number of unique BSTs by building up from smaller subproblems.


# Test Cases
# Test Case 1:
n = 3
sol = Solution()
print(sol.numTrees(n)) # 5

# Test Case 2:
n = 1
sol = Solution()
print(sol.numTrees(n)) # 1
