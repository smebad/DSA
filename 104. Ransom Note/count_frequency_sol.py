# Ransom Note
# Count Frequency Solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False

        return True
    
# Time Complexity: O(m + n), where m is the length of ransomNote and n is the length of magazine. This is because we traverse both strings once to count the characters and then check the counts.
# Space Complexity: O(1), since we use a fixed-size list of 26 integers to count the frequency of characters, which does not depend on the input size.
# This solution is efficient for large inputs as it avoids repeated searching and removal operations, making it much faster than the brute force approach.

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