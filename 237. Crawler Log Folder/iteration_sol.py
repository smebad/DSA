# Crawler Log Folder
# Iteration Solution:
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                res = max(0, res - 1)
            else:
                res += 1
        return res

# Time Complexity: O(n), where n is the number of logs. We iterate through the logs list once.
# Space Complexity: O(1), we use a constant amount of space regardless of the input size.
# This solution is efficient and straightforward, effectively tracking the depth of the current folder in relation to the main folder.


# Test cases:
solution = Solution()
print(solution.minOperations(["d1/","d2/","../","d21/","./"]))  # Output: 2
print(solution.minOperations(["d1/","d2/","./","d3/","../","d31/"]))  # Output: 3
print(solution.minOperations(["d1/","../","../","../"]))  # Output: 0
