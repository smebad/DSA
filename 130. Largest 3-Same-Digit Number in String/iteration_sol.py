# Largest 3-Same-Digit Number in String
# Iteration Solution:

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = "0"

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, num[i : i + 3])

        return "" if res == "0" else res

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

