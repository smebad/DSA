# Fruit Into Baskets - LeetCode

## Problem Explanation

The **"Fruit Into Baskets"** problem is a popular sliding window problem from LeetCode. You are given an integer array `fruits`, where each element represents a type of fruit growing on a tree in a row. You can pick fruits starting from any tree, but you have only **two baskets**, and each basket can hold only **one type of fruit**.

You must pick **one fruit from every consecutive tree** moving to the right, until you reach a tree with a fruit type that does not fit in your two baskets. The goal is to find the **maximum number of fruits** you can collect in total under these rules.

### Rules Recap:

1. You can have only two baskets.
2. Each basket can hold only one type of fruit.
3. You must pick from consecutive trees.
4. You must stop when encountering a third type of fruit.

### Example

**Input:** `fruits = [1,2,3,2,2]`
**Output:** `4`
**Explanation:** Pick fruits from trees `[2,3,2,2]`. You can carry two types of fruits: 2 and 3. The total collected fruits are 4.

---

## Code Implementation (Sliding Window Approach)

```python
from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)  # Dictionary to store fruit counts in the current window
        l, total, res = 0, 0, 0   # Initialize left pointer, current total fruits, and result

        for r in range(len(fruits)):  # Iterate using right pointer
            count[fruits[r]] += 1     # Add the current fruit to the count
            total += 1                # Increment total fruits in the current window

            # If more than 2 types of fruits are in the window, shrink it from the left
            while len(count) > 2:
                f = fruits[l]          # Fruit at left pointer
                count[f] -= 1          # Remove one occurrence of that fruit
                total -= 1             # Decrease the window size
                l += 1                 # Move left pointer forward
                if not count[f]:       # If count becomes zero, remove it from dictionary
                    count.pop(f)

            res = max(res, total)      # Update maximum fruits collected

        return res
```

---

## Step-by-Step Logic

1. **Sliding Window Setup:**
   Use two pointers (`l` and `r`) to represent a window over the array.

2. **Counting Fruits:**
   As you expand the right pointer `r`, add the current fruit to a `count` dictionary.

3. **Maintaining Two Fruit Types:**
   If the number of unique fruit types exceeds two, move the left pointer `l` to shrink the window until only two fruit types remain.

4. **Tracking Maximum Fruits:**
   After each valid window adjustment, update the result with the maximum total fruits collected.

5. **End Condition:**
   Continue until all trees are processed. The result `res` will contain the largest number of fruits that can be picked consecutively while following the rules.

---

## Intuition and Explanation

* Imagine you are walking through the trees with two baskets in your hands.
* Each time you see a fruit, check if you can place it in one of your baskets.
* If it’s a new type and both baskets are already occupied, you must discard fruits from the earliest tree until one basket becomes free.
* This continuous process ensures you always have the **largest possible segment** of trees with at most two fruit types.

The **sliding window** method efficiently simulates this process without having to restart counting for every possible starting tree.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`
  We traverse the array once using the right pointer, and the left pointer moves only forward. Thus, the total operations are linear in the size of the array.

* **Space Complexity:** `O(1)`
  The `count` dictionary stores at most **3 fruit types**, which is constant space regardless of input size.

---

## Why This Solution is Optimal

This sliding window approach is optimal because:

1. It examines each element at most twice (once by the right pointer, once by the left pointer).
2. It uses constant extra space.
3. It dynamically maintains the longest valid subarray without restarting the process from scratch.

Any alternative (like brute force checking all subarrays) would have a time complexity of `O(n^2)` or worse, making this method the most efficient and scalable for large inputs.

---

## Test Cases

```python
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
```