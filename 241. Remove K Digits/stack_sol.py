# Remove K Digits
# Stack solution:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        stack = stack[:len(stack) - k]
        res = "".join(stack)

        return str(int(res)) if res else "0"

# Time Complexity: O(n), where n is the length of the input string num. Each digit is processed at most twice (once pushed onto the stack and once popped).
# Space Complexity: O(n) in the worst case, where all digits are pushed onto the stack.
# This stack solution efficiently removes k digits to form the smallest possible number by maintaining a monotonically increasing stack.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    num1 = "1432219"
    k1 = 3
    print(solution.removeKdigits(num1, k1))  # Expected Output: "1219"

    # Test Case 2
    num2 = "10200"
    k2 = 1
    print(solution.removeKdigits(num2, k2))  # Expected Output: "200"

    # Test Case 3
    num3 = "10"
    k3 = 2
    print(solution.removeKdigits(num3, k3))  # Expected Output: "0"

    # Additional Test Case 4
    num4 = "123456"
    k4 = 3
    print(solution.removeKdigits(num4, k4))  # Expected Output: "123"

    # Additional Test Case 5
    num5 = "7654321"
    k5 = 4
    print(solution.removeKdigits(num5, k5))  # Expected Output: "321"
