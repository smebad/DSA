# Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


# Frequency Count Solution:
from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)

        return res
    
# Time Complexity: O(n * m), where n is the number of words and m is the average length of the words. This is because we iterate through each word and for each word, we count the frequency of characters which takes O(m) time.
# Space Complexity: O(1), since the hashmap will contain at most 26 entries (one for each lowercase English letter), which is a constant space.
# This frequency count solution is efficient and works well within the given constraints.


# Test Cases:
sol = Solution()

# Test Case 1:
words1 = ["bella","label","roller"]
print(sol.commonChars(words1))  # Expected Output: ["e","l","l"]

# Test Case 2:
words2 = ["cool","lock","cook"]
print(sol.commonChars(words2))  # Expected Output: ["c","o"]