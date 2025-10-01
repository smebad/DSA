# Take Gifts From the Richest Pile
# Max-Heap Solution:
import heapq
from math import floor, sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(n)))

        return -sum(gifts)

# Time Complexity: O(n + k log n), where n is the number of piles and k is the number of seconds. We build the max-heap in O(n) time and each of the k operations takes O(log n) time.
# Space Complexity: O(n), for storing the max-heap.
# This solution efficiently simulates the process of taking gifts from the richest pile using a max-heap.


# Test Cases:
sol = Solution()

# Test Case 1:
gifts = [25,64,9,4,100]
k = 4
print(sol.pickGifts(gifts, k))  # Output: 29

# Test Case 2:
gifts = [1,1,1,1]
k = 4
print(sol.pickGifts(gifts, k))  # Output: 4
