# Unique Email Addresses
# Iteration Solution:
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i + 1:]
            unique.add((local, domain))
        return len(unique)
    
# Time Complexity: O(n * m), where n is the number of emails and m is the average length of each email. This is because we iterate through each email and perform operations like checking characters and constructing local names.
# Space Complexity: O(n), where n is the number of unique emails stored in the set unique.
# This solution uses iteration to manually parse the local and domain parts of each email, avoiding built-in string methods like split and replace.


# Test Cases
# Test Case 1:
emails1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails1)) # Expected Output: 2

# Test Case 2:
emails2 = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
print(Solution().numUniqueEmails(emails2)) # Expected Output: 3
