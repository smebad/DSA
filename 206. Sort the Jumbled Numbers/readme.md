# Sort the Jumbled Numbers - LeetCode

## 1. Problem Explanation

In this problem, you are given:

* An array `mapping` of size 10, where `mapping[i] = j` means digit `i` is replaced with digit `j`.
* An integer array `nums`.

Each number in `nums` is transformed by replacing every digit using the given `mapping`. This transformed number is called the **mapped value**.

Your task is to sort the original `nums` array based on these mapped values, while following these rules:

* Sorting is done using the mapped values, not the original numbers.
* If two numbers have the same mapped value, they must keep their original order (stable sort).
* The final output must contain the original numbers, not the mapped ones.

---

## 2. Code with Comments

```python
from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []  # This will store (mapped_value, original_index)

        for i, n in enumerate(nums):
            n = str(n)        # Convert the number to a string to process digit by digit
            mapped_n = 0     # This will store the mapped value of the number

            for c in n:      # Process each digit
                mapped_n *= 10                     # Shift left by one digit
                mapped_n += mapping[int(c)]       # Add mapped digit

            # Store mapped value with original index to preserve order in ties
            pairs.append((mapped_n, i))

        # Sort based on mapped value (Python sort is stable)
        pairs.sort()

        # Return the original numbers in sorted mapped order
        return [nums[p[1]] for p in pairs]
```

---

## 3. Solution Approach and Logic (Beginner-Friendly Explanation)

### Step 1: Convert Numbers Using the Mapping

Each number is broken into its digits. Every digit is replaced using the `mapping` array. These new digits form the mapped value.

Example:

```
Original: 991
Mapping: 9 -> 6, 1 -> 9
Mapped Value: 669
```

### Step 2: Store Mapped Values with Original Positions

We store each number as a pair:

```
(mapped_value, original_index)
```

This is important because if two numbers share the same mapped value, we must preserve their original order.

### Step 3: Sort the Pairs

We sort the list of pairs using the mapped values. Python's sort is **stable**, so elements with equal mapped values keep their original order automatically.

### Step 4: Build the Final Answer

After sorting, we use the stored original indices to rebuild the answer using the original values from `nums`.

---

## 4. Time and Space Complexity Analysis

### Time Complexity

* Mapping each number takes O(d), where d is the number of digits (at most 10).
* For `n` numbers, this becomes O(n).
* Sorting `n` elements takes O(n log n).

Total Time Complexity:

```
O(n log n)
```

### Space Complexity

* We store `n` pairs in an auxiliary list.

Total Space Complexity:

```
O(n)
```

---

## 5. Why This Solution Is Optimal

* We must sort the array, and comparison-based sorting has a lower bound of O(n log n).
* The digit mapping process is already optimized and cannot be avoided.
* Stability is required by the problem, and this method guarantees correct ordering.

Therefore, this solution is optimal for this problem.

---

## 6. Test Cases
```python
sol = Solution()

# Test Case 1:
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
print(sol.sortJumbled(mapping, nums))  # Expected Output: [338, 38, 991]

# Test Case 2:
mapping = [0,1,2,3,4,5,6,7,8,9]
nums = [789,456,123]
print(sol.sortJumbled(mapping, nums))  # Expected Output: [123, 456, 789]

```
