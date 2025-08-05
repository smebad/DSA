# Length of Last Word
# Built-in function Solution:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())
    
# Time Complexity: O(n), where n is the length of the string s. The split operation traverses the string to create a list of words, and pop retrieves the last word.
# Space Complexity: O(n), as the split operation creates a list of words, which can take up space proportional to the number of words in the string.
# This solution uses Python's built-in string methods to split the string into words and then retrieves the last word's length. However, it is not recommended to use this method for interview scenarios where efficiency is crucial, as it creates an intermediate list of words.


# Test Cases
# Test Case 1:
s1 = "Hello World"
solution1 = Solution()
print(solution1.lengthOfLastWord(s1))  # Output: 5

# Test Case 2:
s2 = "   fly me   to   the moon  "
solution2 = Solution()
print(solution2.lengthOfLastWord(s2))  # Output: 4

# Test Case 3:
s3 = "luffy is still joyboy"
solution3 = Solution()
print(solution3.lengthOfLastWord(s3))  # Output: 6
