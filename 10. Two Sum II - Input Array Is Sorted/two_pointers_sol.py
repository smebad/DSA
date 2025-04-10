# Two Sum II - Input Array Is Sorted

# Two sum (optimal) solution:
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    
# Time complexity: O(n)
# Space complexity: O(1)
# The two pointers solution is more efficient than the brute force solution.
# The two pointers solution is more efficient than the hashmap solution.


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
