# Ransom Note
# Brute Force Solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)

        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                magazine.remove(c)
        
        return True
    
# Time Complexity: O(m * n), where m is the length of ransomNote and n is the length of magazine. This is because for each character in ransomNote, we may need to search through the magazine list to find it.
# Space Complexity: O(n), where n is the length of magazine, as we convert magazine to a list. The space used for the ransomNote is negligible in comparison since it is not stored in a separate data structure.
# This solution is efficient for small inputs but can be slow for larger inputs due to the repeated searching and removal operations in the list. A more efficient solution would involve using a frequency count of characters.

# Test Cases
# Test Case 1:
ransomNote1 = "a"
magazine1 = "b"
solution1 = Solution()
print(solution1.canConstruct(ransomNote1, magazine1))  # Output: False

# Test Case 2:
ransomNote2 = "aa"
magazine2 = "ab"
solution2 = Solution()
print(solution2.canConstruct(ransomNote2, magazine2))  # Output: False

# Test Case 3:
ransomNote3 = "aa"
magazine3 = "aab"
solution3 = Solution()
print(solution3.canConstruct(ransomNote3, magazine3))  # Output: True