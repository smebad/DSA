# Adding Spaces to a String
# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

 

# Example 1:

# Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
# Output: "Leetcode Helps Me Learn"
# Explanation: 
# The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
# We then place spaces before those characters.
# Example 2:

# Input: s = "icodeinpython", spaces = [1,5,7,9]
# Output: "i code in py thon"
# Explanation:
# The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
# We then place spaces before those characters.
# Example 3:

# Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
# Output: " s p a c i n g"
# Explanation:
# We are also able to place spaces before the first character of the string.
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists only of lowercase and uppercase English letters.
# 1 <= spaces.length <= 3 * 105
# 0 <= spaces[i] <= s.length - 1
# All the values of spaces are strictly increasing.


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