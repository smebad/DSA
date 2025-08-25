# Find First Palindromic String in the Array
# Reverse String Solution:
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""

# Time Complexity: O(n * m) where n is the number of words and m is the average length of the words. This is because we are checking each word to see if it is equal to its reverse, which takes O(m) time, and we do this for each of the n words.
# Space Complexity: O(1) since we are not using any additional space that grows with the input size.
# This reverse string solution is efficient for the given problem constraints.

# Test Cases
sol = Solution()

# Test Case 1:
words1 = ["abc","car","ada","racecar","cool"]
print(sol.firstPalindrome(words1))  # Output: "ada"

# Test Case 2:
words2 = ["notapalindrome","racecar"]
print(sol.firstPalindrome(words2))  # Output: "racecar"

# Test Case 3:
words3 = ["def","ghi"]
print(sol.firstPalindrome(words3))  # Output: ""

