# Alternating Groups II
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

# Example 1:

# Input: colors = [0,1,0,1,0], k = 3

# Output: 3

# Explanation:



# Alternating groups:



# Example 2:

# Input: colors = [0,1,0,0,1,0,1], k = 6

# Output: 2

# Explanation:



# Alternating groups:



# Example 3:

# Input: colors = [1,1,0,1], k = 4

# Output: 0

# Explanation:



 

# Constraints:

# 3 <= colors.length <= 105
# 0 <= colors[i] <= 1
# 3 <= k <= colors.length

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