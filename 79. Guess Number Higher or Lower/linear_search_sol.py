# Guess Number Higher or Lower
# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

 

# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:

# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 231 - 1
# 1 <= pick <= n


# Binary Search Solution:


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