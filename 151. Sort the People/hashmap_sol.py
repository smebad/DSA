# Sort the People
# Hashmap Solution:
from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = {}
        for h, n in zip(heights, names):
            height_to_name[h] = n

        res = []
        for h in reversed(sorted(heights)):
            res.append(height_to_name[h])

        return res

# Time Complexity: O(n log n), where n is the number of people. This is due to the sorting step. The time complexity is dominated by the sorting operation, which takes O(n log n) time in the worst case.
# Space Complexity: O(n) for storing the height-to-name mapping in the dictionary.
# This hashmap solution is efficient and straightforward, leveraging a dictionary to map heights to names and then sorting the heights to retrieve names in the desired order.


# Test Cases:
sol = Solution()

# Test Case 1:
names1 = ["Mary","John","Emma"]
heights1 = [180,165,170]
print(sol.sortPeople(names1, heights1))  # Output: ["Mary","Emma","John"]

# Test Case 2:
names2 = ["Alice","Bob","Bob"]
heights2 = [155,185,150]
print(sol.sortPeople(names2, heights2))  # Output: ["Bob","Alice","Bob"]
