# Two Sum II - Input Array Is Sorted

# brute force solution:
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
# Time complexity: O(n^2)
# Space complexity: O(1)


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
