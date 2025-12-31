# Adding Spaces to a String
# Two Ponters Solution:
from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, j = 0, 0
        res = []

        while i < len(s) and j < len(spaces):
            if i < spaces[j]:
                res.append(s[i])
                i += 1
            else:
                res.append(' ')
                j += 1
          
        if i < len(s):
            res.append(s[i:])

        return ''.join(res)

# Time Complexity: O(n + m) where n is the length of s and m is the length of spaces
# Space Complexity: O(n + m) for the result list res and the space used for the output string.
# This solution is efficient and works well within the given constraints.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "LeetcodeHelpsMeLearn"
    spaces1 = [8, 13, 15]
    print(solution.addSpaces(s1, spaces1))  # Expected Output: "Leetcode Helps Me Learn"

    # Test Case 2
    s2 = "Icodeinpython"
    spaces2 = [1, 5, 7, 9]
    print(solution.addSpaces(s2, spaces2))  # Expected Output: "i code in py thon"

    # Test Case 3
    s3 = "spacing"
    spaces3 = [0, 1, 2, 3, 4, 5, 6]
    print(solution.addSpaces(s3, spaces3))  # Expected Output: " s p a c i n g"
