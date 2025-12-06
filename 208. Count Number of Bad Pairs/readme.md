# Count Number of Bad Pairs - LeetCode

## 1. Problem Explanation

You are given a 0-indexed integer array `nums`. A pair of indices `(i, j)` is called a **bad pair** if:

* `i < j`, and
* `j - i != nums[j] - nums[i]`

Your task is to count how many such **bad pairs** exist in the array.

### Key Idea

If:

```
j - i == nums[j] - nums[i]
```

Then the pair is a **good pair**. Otherwise, it is a **bad pair**.

So instead of directly counting bad pairs, we:

1. Count all possible index pairs
2. Subtract the number of good pairs

### Example

**Input:** `[4, 1, 3, 3]`

All index pairs `(i, j)` with `i < j`:

* (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)

Only one pair is good. The rest 5 are bad.

**Output:** `5`

---

## 2. Code With Detailed Comments

```python
from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0          # Stores number of good pairs found so far
        total_pairs = 0         # Stores total possible pairs (i < j)
        count = defaultdict(int)  # Stores frequency of (nums[i] - i)

        for i in range(len(nums)):
            total_pairs += i   # Number of pairs formed with index i

            # Count how many previous indices had same (nums[j] - j)
            good_pairs += count[nums[i] - i]

            # Store the value nums[i] - i in the hashmap
            count[nums[i] - i] += 1

        # Total bad pairs = total pairs - good pairs
        return total_pairs - good_pairs
```

---

## 3. Solution, Approach, and Logic

### Step 1: Understanding Good Pairs

From the condition:

```
j - i == nums[j] - nums[i]
```

Rearranging:

```
nums[i] - i == nums[j] - j
```

This means a pair is **good** if both indices have the same value of:

```
nums[index] - index
```

So instead of checking `(i, j)` directly, we simply check how many times the same `(nums[i] - i)` value appears.

---

### Step 2: Counting Total Pairs

For an array of size `n`, total possible `(i, j)` pairs where `i < j` is:

```
0 + 1 + 2 + ... + (n-1)
```

We accumulate this gradually using:

```
total_pairs += i
```

---

### Step 3: Counting Good Pairs Using HashMap

We use a hashmap where keys are `(nums[i] - i)` and values are how many times each key has appeared so far.

At each index `i`:

* We check how many times `nums[i] - i` already appeared
* That count directly adds to the number of good pairs

---

### Step 4: Calculating Bad Pairs

Since:

```
Bad Pairs = Total Pairs - Good Pairs
```

We simply return:

```
total_pairs - good_pairs
```

---

### Why This Approach Is Efficient

A brute-force approach would check all `(i, j)` pairs which takes `O(n²)` time and will be too slow for large inputs.

This optimized approach turns the problem into a frequency counting problem and solves it in `O(n)` time.

---

## 4. Time and Space Complexity

### Time Complexity

You traverse the array once and each hashmap operation takes `O(1)` on average.

```
Time Complexity = O(n)
```

---

### Space Complexity

The hashmap stores values of `(nums[i] - i)`. In the worst case, all values are unique.

```
Space Complexity = O(n)
```

---

## 5. Most Optimal Solution

The provided **HashMap-based solution** is the most optimal.

### Why It Is Optimal

* It avoids nested loops
* It avoids checking each possible pair
* It transforms the problem using a mathematical identity
* It runs in linear time which is the best possible for this problem

Any solution must look at all elements at least once, so `O(n)` is the theoretical lower bound.

---

## 6. Test Cases

```python
# Test Case 1
nums1 = [4, 1, 3, 3]
print(solution.countBadPairs(nums1))  # Output: 5

# Test Case 2
nums2 = [1, 2, 3, 4, 5]
print(solution.countBadPairs(nums2))  # Output: 0
```