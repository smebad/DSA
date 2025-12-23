# Maximum Distance in Arrays - LeetCode

## Problem Description

"Maximum Distance in Arrays" is a problem where you are given `m` arrays, each sorted in ascending order. You need to pick one integer from two different arrays and calculate the distance between them. The distance between two integers `a` and `b` is defined as `|a - b|`.

Your task is to find the **maximum distance** possible by picking one integer from two different arrays.

### Example 1:

```
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: Pick 1 from the first or third array and 5 from the second array. Distance = |1 - 5| = 4.
```

### Example 2:

```
Input: arrays = [[1],[1]]
Output: 0
Explanation: Only one way to pick numbers from different arrays, distance = |1 - 1| = 0.
```

### Constraints:

* `m == arrays.length`
* `2 <= m <= 10^5`
* `1 <= arrays[i].length <= 500`
* `-10^4 <= arrays[i][j] <= 10^4`
* `arrays[i]` is sorted in ascending order.
* Total integers across all arrays ≤ 10^5

## Solution

```python
from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize current minimum and maximum values from the first array
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        res = 0

        # Iterate over the remaining arrays
        for i in range(1, len(arrays)):
            arr = arrays[i]
            # Update the maximum distance using current array's first and last elements
            res = max(
                res,
                arr[-1] - cur_min,  # distance from current array's max to global min
                cur_max - arr[0]     # distance from global max to current array's min
            )
            
            # Update global min and max for future comparisons
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        return res
```

### Step-by-Step Comments:

1. `cur_min, cur_max = arrays[0][0], arrays[0][-1]`: Initialize the minimum and maximum values with the first array.
2. `res = 0`: Store the maximum distance found.
3. Loop through arrays starting from the second one.
4. For each array, check two possible distances:

   * Distance from this array's maximum to the global minimum seen so far.
   * Distance from the global maximum to this array's minimum.
5. Update `res` with the maximum of these distances.
6. Update `cur_min` and `cur_max` to include the current array for future comparisons.
7. Return `res` after checking all arrays.

## Solution Logic & Approach

* Since each array is sorted, the **minimum** and **maximum** of an array are at the edges.
* To maximize `|a - b|` where `a` and `b` come from different arrays:

  * Compare the largest element of the current array with the smallest element seen so far.
  * Compare the smallest element of the current array with the largest element seen so far.
* Keep updating the global min and max as we iterate through arrays.
* This approach ensures we only need to check **edge elements**, making it very efficient.

### Why this is optimal

* **Time Complexity:** `O(m)`, where `m` is the number of arrays, since we visit each array once.
* **Space Complexity:** `O(1)`, only using a few variables.
* This is optimal because we do not need to check all pairs of numbers across arrays, only the edges.

## Test Cases

```python
solution = Solution()

# Test Case 1
arrays1 = [[1,2,3],[4,5],[1,2,3]]
print(solution.maxDistance(arrays1))  # Output: 4

# Test Case 2
arrays2 = [[1],[1]]
print(solution.maxDistance(arrays2))  # Output: 0

# Additional Test Case 3
arrays3 = [[-10,0,5],[7,10],[2,8]]
print(solution.maxDistance(arrays3))  # Output: 20 (5 - (-10))
```