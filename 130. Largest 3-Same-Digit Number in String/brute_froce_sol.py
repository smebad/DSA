# Largest 3-Same-Digit Number in String
# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
 

# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:

# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:

# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 

# Constraints:

# 3 <= num.length <= 1000
# num only consists of digits.


# Brute Force Solution:
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        val = 0

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                tmp = num[i : i + 3]
                if val <= int(tmp):
                    val = int(tmp)
                    res = tmp

        return res

# Time Complexity: O(n), where n is the length of the input string. In this approach, we are iterating through the string once.
# Space Complexity: O(1), as we are using a constant amount of space for variables.
# This approach is efficient and works well within the given constraints.


# Test Cases
sol = Solution()

# Test Case 1:
num1 = "6777133339"
print(sol.largestGoodInteger(num1))  # Output: "777"

# Test Case 2:
num2 = "2300019"
print(sol.largestGoodInteger(num2))  # Output: "000"

# Test Case 3:
num3 = "42352338"
print(sol.largestGoodInteger(num3))  # Output: ""
