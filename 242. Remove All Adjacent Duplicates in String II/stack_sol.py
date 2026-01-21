# Remove All Adjacent Duplicates in String II
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
