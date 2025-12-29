# Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

 

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:

# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:

# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
 

# Constraints:

# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.


# Two Pointers Solution:
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = 0  # Index of word
        i = j = 0    # Index of character

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False

            i, j = i + 1, j + 1

            if i == len(word1[w1]):
                w1 += 1
                i = 0
            if j == len(word2[w2]):
                w2 += 1
                j = 0

        return w1 == len(word1) and w2 == len(word2)

# Time Complexity: O(n + m), where n and m are the total lengths of the strings formed by word1 and word2 respectively.
# Space Complexity: O(1), as we are using only a constant amount of extra space.
# This two point is efficient because it avoids the overhead of string concatenation and directly compares characters from both arrays.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert solution.arrayStringsAreEqual(word1, word2) == True

    # Test Case 2
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert solution.arrayStringsAreEqual(word1, word2) == False

    # Test Case 3
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    assert solution.arrayStringsAreEqual(word1, word2) == True

    # Test Case 4
    word1 = ["hello", "world"]
    word2 = ["helloworld"]
    assert solution.arrayStringsAreEqual(word1, word2) == True

    # Test Case 5
    word1 = ["a", "b", "c"]
    word2 = ["a", "b", "d"]
    assert solution.arrayStringsAreEqual(word1, word2) == False

    print("All test cases passed!")