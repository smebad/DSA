
# Sorting Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
# Time and Space Complexity: 
# O(n log n + m log m) for sorting both strings, where n and m are the lengths of the two strings.
# O(1) or O(n+m) for the space complexity, depending on the sorting algorithm used.

# Test Cases:

# Test Case 1
s = "carrace"
t = "racecar"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: False

# Test Case 2
s = "hello"
t = "world"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: False
