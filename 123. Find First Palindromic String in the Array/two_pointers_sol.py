# Find First Palindromic String in the Array
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

