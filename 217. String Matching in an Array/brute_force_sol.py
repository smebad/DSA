# String Matching in an Array
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
