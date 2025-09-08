# Redistribute Characters to Make All Strings Equal
# Hashmap Solution:
from typing import List
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_cnt = defaultdict(int)

        for w in words:
            for c in w:
                char_cnt[c] += 1

        for c in char_cnt:
            if char_cnt[c] % len(words):
                return False
        return True
    
# Time Complexity: O(n * m), where n is the number of words and m is the average length of the words. This is because we are checking each word to see if it is equal to its reverse, which takes O(m) time, and we do this for each of the n words.
# Space Complexity: O(1), since the hashmap will contain at most 26 entries (one for each lowercase English letter), which is a constant space.
# This hashmap solution efficiently counts the occurrences of each character across all words and checks if they can be evenly distributed among the words.


# Test Cases
sol = Solution()

# Test Case 1:
words1 = ["abc","aabc","bc"]
print(sol.makeEqual(words1))  # Expected output: True

# Test Case 2:
words2 = ["ab","a"]
print(sol.makeEqual(words2))  # Expected output: False
