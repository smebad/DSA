# Fruit Into Baskets
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 

# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length


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