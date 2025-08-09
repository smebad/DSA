# Isomorphic Strings
# Hashmap solution:

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True
    
# Time Complexity: O(n), where n is the length of the strings. The function iterates through each character of the strings once.
# Space Complexity: O(m), where m is the number of unique characters in the strings. The function uses two dictionaries to store the mappings.
# This hashmap solution efficiently checks if two strings are isomorphic by maintaining a mapping of characters from one string to the other and vice versa. If any character mapping conflicts, it returns False. If all characters can be mapped without conflict, it returns True.

# Test Cases
# Test Case 1:
s1 = "egg"
t1 = "add"
sol = Solution()
print(sol.isIsomorphic(s1, t1))  # Expected output: True

# Test Case 2:
s2 = "foo"
t2 = "bar"
print(sol.isIsomorphic(s2, t2))  # Expected output: False

# Test Case 3:
s3 = "paper"
t3 = "title"
print(sol.isIsomorphic(s3, t3))  # Expected output: True

