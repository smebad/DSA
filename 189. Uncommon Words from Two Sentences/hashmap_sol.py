# Uncommon Words from Two Sentences
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
