# Fruit Into Baskets

# Sliding Window Solution:
from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)

            res = max(res, total)

        return res
    
# Time Complexity: O(n), where n is the length of the fruits array. We traverse the array once with the right pointer, and the left pointer only moves forward. The while loop runs at most n times, where n is the length of the fruits array.
# Space Complexity: O(1), since the count dictionary will hold at most 3 different fruit types at any time (due to the problem constraints of having only 2 baskets). Thus, the space used does not scale with the input size.
# This solution efficiently finds the longest subarray with at most two distinct elements using the sliding window technique.


# Test Cases:
solution = Solution()

# Test Case 1:
fruits = [1,2,1]
print(solution.totalFruit(fruits))  # Output: 3

# Test Case 2:
fruits = [0,1,2,2]
print(solution.totalFruit(fruits))  # Output: 3

# Test Case 3:
fruits = [1,2,3,2,2]
print(solution.totalFruit(fruits))  # Output: 4

# Test Case 4:
fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(solution.totalFruit(fruits))  # Output: 5
