# Number of Pairs of Interchangeable Rectangles
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
