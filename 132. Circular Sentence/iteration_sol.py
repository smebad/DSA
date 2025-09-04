# Circular Sentence
# Iteration solution:

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]

# Time Complexity: O(n), where n is the length of the sentence. We iterate through the sentence once.
# Space Complexity: O(1), as we are using a constant amount of extra space.
# This solution is efficient and works well within the given constraints.

# Test Cases
solution = Solution()

# Test Case 1:
sentence = "leetcode exercises sound delightful"
print(solution.isCircularSentence(sentence))  # Output: True

# Test Case 2:
sentence = "eetcode"
print(solution.isCircularSentence(sentence))  # Output: True

# Test Case 3:
sentence = "Leetcode is cool"
print(solution.isCircularSentence(sentence))  # Output: False
