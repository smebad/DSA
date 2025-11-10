# Uncommon Words from Two Sentences
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"

# Output: ["sweet","sour"]

# Explanation:

# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:

# Input: s1 = "apple apple", s2 = "banana"

# Output: ["banana"]

 

# Constraints:

# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.


# Hashmap Solution:
from typing import List
from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = defaultdict(int)
        for w in s1.split(" ") + s2.split(" "):
            count[w] += 1

        res = []
        for w, cnt in count.items():
            if cnt == 1:
                res.append(w)
        return res
    
# Time Complexity: O(n + m), where n and m are the lengths of sentences s1 and s2 respectively. The loop iterates through the words in both sentences, which takes O(n + m) time.
# Space Complexity: O(n + m) in the worst case, where all words in both sentences are unique. The hashmap stores each unique word along with its count.
# This hashmap solution is efficient and straightforward for solving the problem of finding uncommon words from two sentences.


# Test cases:
solution = Solution()

# Test Case 1:
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["sweet", "sour"]

# Test Case 2:
s1 = "apple apple"
s2 = "banana"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["banana"]