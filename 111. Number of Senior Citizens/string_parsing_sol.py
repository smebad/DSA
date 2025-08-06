# Number of Senior Citizens
# String Parsing Solution:
from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            if int(d[11:13]) > 60:
                res += 1
        return res
    
# Time Complexity: O(n), where n is the number of passengers in the details list. We iterate through each passenger's details once.
# Space Complexity: O(1), as we are using a constant amount of space for the result variable.
# This solution efficiently counts the number of senior citizens by checking the age substring in each passenger's details string. It avoids unnecessary string operations and directly accesses the relevant characters for age comparison.

# Test Cases
# Test Case 1:
print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])) # 2

# Test Case 2:
print(Solution().countSeniors(["1313579440F2036","2921522980M5644"])) # 0
