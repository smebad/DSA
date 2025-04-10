# Two Sum II - Input Array Is Sorted

# hashmap solution:
from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []
    
# Time complexity: O(n)
# Space complexity: O(n)
# The hashmap solution is more efficient than the brute force solution.


# Test cases:
# Test Case 1:
sol = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(sol.twoSum(numbers, target))  # Output: [1, 2]

# Test Case 2:
sol = Solution()
numbers = [2, 3, 4]
target = 6
print(sol.twoSum(numbers, target))  # Output: [1, 3]

# Test Case 3:
sol = Solution()
numbers = [-1, 0]
target = -1
print(sol.twoSum(numbers, target))  # Output: [1, 2]
