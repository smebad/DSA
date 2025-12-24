# String Matching in an Array
# Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.


# Brute Force Solution:
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res

# Time Complexity: O(n^2 * m^2) where n is the number of words and m is the average length of the words.
# Space Complexity: O(k) where k is the number of substrings found.
# This brute force solution is straightforward but may not be efficient for large inputs.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    words1 = ["mass","as","hero","superhero"]
    print(solution.stringMatching(words1))  # Expected Output: ["as","hero"]

    # Test Case 2
    words2 = ["leetcode","et","code"]
    print(solution.stringMatching(words2))  # Expected Output: ["et","code"]

    # Test Case 3
    words3 = ["blue","green","bu"]
    print(solution.stringMatching(words3))  # Expected Output: []