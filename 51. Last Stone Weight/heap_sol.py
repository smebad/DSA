# Last Stone Weight
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
