# Check If a String Contains All Binary Codes of Size K
# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s[i] is either '0' or '1'.
# 1 <= k <= 20

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
