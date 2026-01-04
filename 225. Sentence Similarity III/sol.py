# Sentence Similarity III
# Solution:
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s2) < len(s1):
            s1, s2 = s2, s1

        l1 = 0
        while l1 < len(s1) and s1[l1] == s2[l1]:
            l1 += 1

        r1, r2 = len(s1) - 1, len(s2) - 1
        while r1 >= l1 and r2 >= 0 and s1[r1] == s2[r2]:
            r1, r2 = r1 - 1, r2 - 1

        return l1 > r1

# Time Complexity: O(min(n, m)), where n and m are the lengths of sentence1 and sentence2 respectively.
# Space Complexity: O(1) excluding the space used for splitting the sentences into words.
# This solution efficiently checks for sentence similarity by comparing words from the start and end of both sentences.


# Test Cases:
# Test Case 1:
sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(Solution().areSentencesSimilar(sentence1, sentence2))  # Output: True

# Test Case 2:
sentence1 = "of"
sentence2 = "A lot of words"
print(Solution().areSentencesSimilar(sentence1, sentence2))  # Output: False

# Test Case 3:
sentence1 = "Eating right now"
sentence2 = "Eating"
print(Solution().areSentencesSimilar(sentence1, sentence2))  # Output: True
