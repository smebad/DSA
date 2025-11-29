# Minimum Number of Operations to Make Array Empty - LeetCode

## 1. Problem Explanation

You are given a 0-indexed array `nums` containing only positive integers. You can perform two types of operations any number of times:

1. Remove exactly **two equal elements** from the array.
2. Remove exactly **three equal elements** from the array.

Your goal is to **empty the entire array using the minimum number of operations**. If it is **not possible to remove all elements**, return `-1`.

### Key Points of the Problem

* You can only remove elements in groups of 2 or 3.
* All removed elements in one operation must have the **same value**.
* You must minimize the total number of operations.
* If any number appears only once, it is **impossible** to remove it.

### Example

Input: `nums = [2,3,3,2,2,4,2,3,4]`
Output: `4`

This means the array can be completely emptied in exactly 4 valid operations, and no solution with fewer operations exists.

Input: `nums = [2,1,2,2,3,3]`
Output: `-1`

This means it is impossible to make the array empty using the given rules.

---

## 2. Code With Comments

Below is your exact solution with added comments to explain each step clearly:

```python
from collections import Counter
from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count the frequency of each number in the array
        count = Counter(nums)
        
        # This will store the total number of operations
        res = 0

        # Loop through each unique number and its frequency
        for num, cnt in count.items():
            # If any number appears only once, it cannot be removed
            # because we need at least 2 equal elements
            if cnt == 1:
                return -1
            
            # Divide the frequency by 3 and take the ceiling
            # This ensures we use as many groups of 3 as possible
            res += math.ceil(cnt / 3)

        # Return the total operations needed
        return res
```

---

## 3. Solution Approach, Logic, and Explanation

### Main Idea

The key idea is to:

1. **Count how many times each number appears**.
2. For each number, determine the **minimum operations needed** to remove all its occurrences.
3. **Add all operations together** to get the final answer.

---

### Step 1: Count Frequencies

We use `Counter(nums)` to count how many times each number appears.

Example:

```
nums = [2,3,3,2,2,4,2,3,4]
count = {2: 4, 3: 3, 4: 2}
```

---

### Step 2: Handle Impossible Case

If any number appears **only once**, then:

* You cannot delete it using 2 or 3 removals.
* So the answer must be `-1` immediately.

This is why the code checks:

```
if cnt == 1:
    return -1
```

---

### Step 3: Greedy Strategy

We always try to remove elements in **groups of 3 first**, because:

* Removing 3 elements in one operation is more efficient than removing 2.
* It minimizes the total number of operations.

To calculate this properly, we use:

```
math.ceil(cnt / 3)
```

This gives the **minimum number of operations needed** for that number.

Examples:

* If `cnt = 2` → `ceil(2/3) = 1` operation
* If `cnt = 3` → `ceil(3/3) = 1` operation
* If `cnt = 4` → `ceil(4/3) = 2` operations
* If `cnt = 5` → `ceil(5/3) = 2` operations
* If `cnt = 6` → `ceil(6/3) = 2` operations

This works because combinations of 2 and 3 always cover all valid cases **except when cnt = 1**.

---

### Step 4: Final Answer

We add the operations for each number to `res` and return it.

---

## 4. Time and Space Complexity Analysis

### Time Complexity

* Counting elements using `Counter` takes `O(n)`.
* Looping through the frequency map takes `O(k)`, where `k` is the number of unique elements.
* Overall time complexity is:

```
O(n)
```

This is optimal because every element must be read at least once.

---

### Space Complexity

* The `Counter` stores `k` unique elements.
* Therefore, space complexity is:

```
O(k)
```

---

## 5. Why This Solution Is Optimal

1. It processes the array in a **single pass**.
2. It uses a **greedy strategy** that always minimizes the number of operations.
3. It correctly handles all edge cases, including impossible cases.
4. No unnecessary loops or extra data structures are used.

Because of these reasons, this solution is both **time-efficient and memory-efficient**, making it the most optimal approach for this problem.

---

## 6. Test Cases Used

```python
solution = Solution()

# Test Case 1
nums1 = [2,3,3,2,2,4,2,3,4]
print(solution.minOperations(nums1))  # Expected output: 4

# Test Case 2
nums2 = [2,1,2,2,3,3]
print(solution.minOperations(nums2))  # Expected output: -1
```