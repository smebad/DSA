# Sort the People
# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

# Constraints:

# n == names.length == heights.length
# 1 <= n <= 103
# 1 <= names[i].length <= 20
# 1 <= heights[i] <= 105
# names[i] consists of lower and upper case English letters.
# All the values of heights are distinct.


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