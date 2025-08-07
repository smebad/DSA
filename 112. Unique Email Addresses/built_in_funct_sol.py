# Unique Email Addresses
# Built-in Functions Solution:
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split('@')
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)
    
# Time Complexity: O(n * m), where n is the number of emails and m is the average length of each email. This is because we iterate through each email and perform operations like splitting and replacing characters.
# Space Complexity: O(n), where n is the number of unique emails stored in the set unique.


# Test Cases
# Test Case 1:
emails1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails1)) # Expected Output: 2

# Test Case 2:
emails2 = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
print(Solution().numUniqueEmails(emails2)) # Expected Output: 3
