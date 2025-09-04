# Circular Sentence
# Splitting the strings solution:

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        w = sentence.split(" ")

        for i in range(len(w)):
            if w[i][0] != w[i - 1][-1]:
                return False

        return True
    
# Time Complexity: O(n), where n is the length of the input string sentence. This is because we need to split the string into words and then iterate through each word to check the circular condition.
# Space Complexity: O(n), in the worst case, we may need to store all the words in the sentence, which requires additional space proportional to the length of the input string.
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
