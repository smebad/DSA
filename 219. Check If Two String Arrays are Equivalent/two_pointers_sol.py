# Check If Two String Arrays are Equivalent
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
