# Longest Repeating Character Replacement
# Sliding Window Solution:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
    
# Time Complexity: O(n) where n is the length of s which is the number of characters in the string.
# Space Complexity: O(m) where m is the number of unique characters in the string.
# This sliding window solution is optimal and runs in linear time.
# The space complexity is also reduced to O(m) where m is the number of unique characters in the string.


# Test Cases:
# Test Case 1:
s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k)) # Expected Output: 4

# Test Case 2:
s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k)) # Expected Output: 4
