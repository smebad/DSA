# Length of Last Word
# Iteration Solution:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            i -= 1
            length += 1
        return length
    
# Time Complexity: O(n), where n is the length of the string s. This is because we are iterating through the string once and performing constant time operations for each character.
# Space Complexity: O(1), as we are using a constant amount of space for the variables i and length.
# This solution efficiently finds the length of the last word by skipping trailing spaces and counting characters until a space is encountered, ensuring that we only traverse the necessary part of the string.


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
