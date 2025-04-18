# Valid Parentheses
# Brute force solution:
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
    
# Time complexity: O(n^2), where n is the length of the string s. This is because in the worst case, we have to iterate through the string n times, and for each iteration, we have to check if any of the three pairs of brackets are present in the string. This takes O(n) time, so the overall time complexity is O(n^2).
# Space complexity: O(n), where n is the length of the string s. This is because we are using a new string to store the result after replacing the brackets, which takes O(n) space. In addition, we are also using a constant amount of space for the variables used in the function.
# Brute force solution is not optimal for large inputs as it takes O(n^2) time complexity


# Test Cases:
# Test Case 1
print(Solution().isValid('()')) # True

# Test Case 2
print(Solution().isValid('()[]{}')) # True

# Test Case 3
print(Solution().isValid('(]')) # False

# Test Case 4
print(Solution().isValid('([])')) # True
