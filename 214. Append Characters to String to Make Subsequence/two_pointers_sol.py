# Append Characters to String to Make Subsequence
# Two pointers solution:
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j
    
# Time complexity: O(n + m), where n and m are the lengths of strings s and t respectively.
# Space complexity: O(1), as we are using only a constant amount of extra space.
# This two pointers approach is efficient and works well within the given constraints.


# Test Cases:
# Test Case 1:
s1 = "coaching"
t1 = "coding"
print(Solution().appendCharacters(s1, t1))  # Output: 4

# Test Case 2:
s2 = "abcde"
t2 = "a"
print(Solution().appendCharacters(s2, t2))  # Output: 0

# Test Case 3:
s3 = "z"
t3 = "abcde"
print(Solution().appendCharacters(s3, t3))  # Output: 5
