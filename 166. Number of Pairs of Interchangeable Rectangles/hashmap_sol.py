# Number of Pairs of Interchangeable Rectangles
# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

# Return the number of pairs of interchangeable rectangles in rectangles.

 

# Example 1:

# Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
# Output: 6
# Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
# - Rectangle 0 with rectangle 1: 4/8 == 3/6.
# - Rectangle 0 with rectangle 2: 4/8 == 10/20.
# - Rectangle 0 with rectangle 3: 4/8 == 15/30.
# - Rectangle 1 with rectangle 2: 3/6 == 10/20.
# - Rectangle 1 with rectangle 3: 3/6 == 15/30.
# - Rectangle 2 with rectangle 3: 10/20 == 15/30.
# Example 2:

# Input: rectangles = [[4,5],[7,8]]
# Output: 0
# Explanation: There are no interchangeable pairs of rectangles.
 

# Constraints:

# n == rectangles.length
# 1 <= n <= 105
# rectangles[i].length == 2
# 1 <= widthi, heighti <= 105
 

# Hashmap Solution:
from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        res = 0
        for w, h in rectangles:
            res += count.get(w / h, 0)
            count[w / h] = 1 + count.get(w / h, 0)
        return res
    
# Time Complexity: O(n), where n is the number of rectangles. We iterate through the list of rectangles once.
# Space Complexity: O(n) in the worst case, where all rectangles have different width-to-height ratios and we store each ratio in the hashmap. The hashmap stores the count of each unique width-to-height ratio encountered.
# This hashmap solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1:
print(sol.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]]))  # Expected output: 6

# Test Case 2:
print(sol.interchangeableRectangles([[4,5],[7,8]]))  # Expected output: 0