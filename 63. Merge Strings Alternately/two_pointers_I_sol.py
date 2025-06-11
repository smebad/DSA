# Merge Strings Alternately
# Two Pointers I solution:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
    
# Time Complexity: O(n + m) where n is the length of word1 and m is the length of word2
# Space Complexity: O(n + m) this is because we are creating a list of size n + m
# This two pointers 1 solution is efficient for large inputs as it has a time complexity of O(n + m). It is optimal and works well for the problem.


# Test Cases:
# Test Case 1:
word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2)) # Expected Output: "apbqcr"

# Test Case 2:
word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2)) # Expected Output: "apbqrs"

# Test Case 3:
word1 = "abcd"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2)) # Expected Output: "apbqcd"

