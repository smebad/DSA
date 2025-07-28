# Find Lucky Integer in an Array
# Hash-Map Solution:
from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1

        for num in cnt:
            if num == cnt[num]:
                res = max(num, res)
        
        return res
    
# Time Complexity: O(n), where n is the length of the array. This is because we are counting the frequency of each number in a single pass.
# Space Complexity: O(n), since we are using a hash map to store the frequency of each number.
# This solution is efficient and works well within the constraints (1 <= arr.length <= 500


# Test Cases
# Test Case 1:
solution = Solution()
arr = [2, 2, 3, 4]
print(solution.findLucky(arr))  # Output: 2

# Test Case 2:
arr = [1, 2, 2, 3, 3, 3]
print(solution.findLucky(arr))  # Output: 3

# Test Case 3:
arr = [2, 2, 2, 3, 3]
print(solution.findLucky(arr))  # Output: -1