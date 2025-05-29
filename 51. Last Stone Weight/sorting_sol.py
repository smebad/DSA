# Last Stone Weight
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
