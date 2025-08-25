# Find First Palindromic String in the Array
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

 

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# Example 2:

# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# Example 3:

# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.


# Two-Pointers Solution:
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            l, r = 0, len(w) - 1
            while w[l] == w[r]:
                if l >= r:
                    return w
                l, r = l + 1, r - 1
        return ""

# Time Complexity: O(n * m), where n is the number of words and m is the average length of the words. This is because we are checking each word to see if it is equal to its reverse using two pointers, which takes O(m) time, and we do this for each of the n words.
# Space Complexity: O(1), since we are not using any additional space that grows with the input size.
# This two-pointers solution is efficient for the given problem constraints.

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
