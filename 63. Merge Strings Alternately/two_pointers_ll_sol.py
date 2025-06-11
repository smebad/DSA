# Merge Strings Alternately
# Two Pointers II solution:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])
            i += 1
            j += 1
        return "".join(res)
    
# Time Complexity: O(n + m) where n is the length of word1 and m is the length of word2
# Space Complexity: O(n + m) this is because we are creating a list of size n + m
# This two pointers 2 solution is efficient for large inputs as it has a time complexity of O(n + m). It is optimal and works well for the problem. 


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

