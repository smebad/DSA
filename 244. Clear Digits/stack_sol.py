# Clear Digits
# Stack Solution:
class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        def isdigit(c):
            return ord("0") <= ord(c) <= ord("9")
        
        for i in range(len(s)):
            if isdigit(s[i]):
                res.pop()
            else:
                res.append(s[i])

        return "".join(res)

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n) in the worst case, when there are no digits in the string s.
# This stack base solution is efficient for the given constraints.


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "abc"
    print(solution.clearDigits(s1))  # Expected Output: "abc"

    # Test Case 2
    s2 = "cb34"
    print(solution.clearDigits(s2))  # Expected Output: ""
