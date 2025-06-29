# Guess Number Higher or Lower
# Linear Search Solution:

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Guess API simulation
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        for num in range(1, n + 1):
            if guess(num) == 0:
                return num
            
# Time Complexity: O(n) where n is the range of numbers from 1 to n. This is because we are checking each number in the range.
# Space Complexity: O(1) since we are using a constant amount of space for the variables num and res.
# This is a linear search solution to the problem, which is not optimal but works for small values of n.


# Test Cases
# Test Case 1:
n = 10
pick = 6
sol = Solution()
print(sol.guessNumber(n))  # Output: 6

# Test Case 2:
n = 1
pick = 1
sol = Solution()
print(sol.guessNumber(n))  # Output: 1

# Test Case 3:
n = 2
pick = 1
sol = Solution()
print(sol.guessNumber(n))  # Output: 1
