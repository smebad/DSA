# Remove All Adjacent Duplicates in String II
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
 

# Constraints:

# 1 <= s.length <= 105
# 2 <= k <= 104
# s only contains lowercase English letters.


# Stack Solution:
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()

        return ''.join(char * count for char, count in stack)
    
# Time Complexity: O(n), where n is the length of the string s. We traverse the string once.
# Space Complexity: O(n) in the worst case, where no characters are removed and we store all characters in the stack.
# This stack based approach efficiently handles the problem of removing adjacent duplicates by keeping track of character counts and removing them when they reach the threshold k.


# Test Cases:

# Test Case 1
print(Solution().removeDuplicates('abcd', 2)) # 'abcd'

# Test Case 2
print(Solution().removeDuplicates('deeedbbcccbdaa', 3)) # 'aa'

# Test Case 3
print(Solution().removeDuplicates('pbbcggttciiippooaais', 2)) # 'ps'