
# Hashmap Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
    
# Time and Space Complexity: 
# O(n + m) for the space complexity, where n and m are the lengths of the two strings.
# O(1) since we have at most 26 characters in the English alphabet.

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
