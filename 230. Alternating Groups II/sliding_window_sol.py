# Alternating Groups II
# Sliding Window Solution:
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        l = 0
        res = 0

        for r in range(1, N + k - 1):
            if colors[r % N] == colors[(r - 1) % N]:
                l = r
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                res += 1
        
        return res
    
# Time Complexity: O(n), where n is the length of the colors array. We traverse the array once using a sliding window approach.
# Space Complexity: O(1), as we use a constant amount of extra space regardless of the input size.
# This sliding window approach efficiently counts the number of alternating groups of size k in a circular array.


# Test Cases
solution = Solution()

# Test Case 1:
colors1 = [0, 1, 0, 1, 0]
k1 = 3
print(solution.numberOfAlternatingGroups(colors1, k1))  # Expected output: 3

# Test Case 2:
colors2 = [0, 1, 0, 0, 1, 0, 1]
k2 = 6
print(solution.numberOfAlternatingGroups(colors2, k2))  # Expected output: 2

# Test Case 3:
colors3 = [1, 1, 0, 1]
k3 = 4
print(solution.numberOfAlternatingGroups(colors3, k3))  # Expected output: 0
