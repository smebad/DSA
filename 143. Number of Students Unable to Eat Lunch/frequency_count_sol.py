# Number of Students Unable to Eat Lunch
# Frequency Count Solution:
from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                break

        return res
    
# Time Complexity: O(n), where n is the number of students (or sandwiches). We iterate through the sandwiches list once, and each operation inside the loop (checking and updating the counter) takes O(1) time.
# Space Complexity: O(1), since the counter will only store counts for two types of sandwiches (0 and 1), which is a constant amount of space.
# This solution efficiently counts the number of students unable to eat lunch by leveraging a frequency count of student preferences, avoiding the need for simulating the entire queue process.


# Test Cases:
sol = Solution()

# Test Case 1:
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(sol.countStudents(students, sandwiches))  # Output: 0

# Test Case 2:
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(sol.countStudents(students, sandwiches))  # Output: 3
