# Check If a String Contains All Binary Codes of Size K
# Hashset Solution:
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2 ** k:
            return False

        codeSet = set()
        for i in range(len(s) - k + 1):
            codeSet.add(s[i:i + k])

        return len(codeSet) == 2 ** k
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once to extract all substrings of length k.
# Space Complexity: O(2^k), since we store all unique binary codes of length k in a set.
# This hashset solution is efficient and works well within the given constraints.


# Test Cases:
# Test Case 1:
s = "00110110"
k = 2
print(Solution().hasAllCodes(s, k))  # Output: True

# Test Case 2:
s = "0110"
k = 1
print(Solution().hasAllCodes(s, k))  # Output: True

# Test Case 3:
s = "0110"
k = 2
print(Solution().hasAllCodes(s, k))  # Output: False
