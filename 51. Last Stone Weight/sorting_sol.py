# Last Stone Weight

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:

# Input: stones = [1]
# Output: 1
 

# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


# Sorting solution:
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
                
        return stones[0] if stones else 0
    
# Time Complexity: O(n^2 log n) due to sorting in each iteration. This is because we sort the list of stones in each iteration, and the number of iterations is at most n (the length of the stones list).
# Space Complexity: O(1) if we consider the input list as part of the input space, otherwise O(n) for the space used by the list of stones.
# This solution is not optimal for larger inputs due to the repeated sorting, but it works well within the constraints given (1 <= stones.length <= 30).


# Test Cases:
# Test Case 1:
stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones)) # Expected Output: 1

# Test Case 2:
stones = [1]
print(Solution().lastStoneWeight(stones)) # Expected Output: 1