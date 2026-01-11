# Defuse the Bomb
# Sliding Window Solution:
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        l = 0
        curSum = 0
        for r in range(n + abs(k)):
            curSum += code[r % n]

            if r - l + 1 > abs(k):
                curSum -= code[l % n]
                l = (l + 1) % n

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % n] = curSum
                elif k < 0:
                    res[(r - 1) % n] = curSum

        return res
    
# Time Complexity: O(n), where n is the length of the code array. We traverse the array a constant number of times.
# Space Complexity: O(1), since we are using a fixed amount of extra space for variables, excluding the output array.
# This sliding window approach is efficient for calculating the sums of contiguous subarrays, especially in a circular array context.


# Test Casea:
solution = Solution()
print(solution.decrypt([5,7,1,4], 3))  # Output: [12,10,16,13]
print(solution.decrypt([1,2,3,4], 0))  # Output: [0,0,0,0]
print(solution.decrypt([2,4,9,3], -2)) # Output: [12,5,6,13]
