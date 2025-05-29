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


# Heap solution:
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
    
# Time Complexity: O(n log n) where n is the number of stones. This is because we use a heap to efficiently get the two largest stones in each iteration, and heap operations (push and pop) take O(log n) time.
# Space Complexity: O(n) for the heap storage of the stones.
# This solution is efficient and works well within the constraints given (1 <= stones.length <= 30).
# The heap is used to efficiently get the two largest stones in each iteration, and heap operations (push and pop) take O(log n) time.


# Test Cases:
# Test Case 1:
stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones)) # Expected Output: 1

# Test Case 2:
stones = [1]
print(Solution().lastStoneWeight(stones)) # Expected Output: 1