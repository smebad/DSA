# Subarray Sums Divisible by K - LeetCode

## 1. Problem Explanation

The problem **Subarray Sums Divisible by K** asks us to find the number of non-empty subarrays whose sum is divisible by a given integer `k`.

A **subarray** is a continuous part of an array. For each possible subarray, we calculate its sum and check if it is divisible by `k`. Instead of calculating all possible subarrays directly (which would be inefficient), we can use a more optimal mathematical approach.

### Example

**Input:** `nums = [4, 5, 0, -2, -3, 1]`, `k = 5`
**Output:** `7`
**Explanation:** There are 7 subarrays whose sum is divisible by 5:

```
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

---

## 2. Code with Comments

```python
from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0  # Tracks the cumulative sum up to the current index
        res = 0  # Counts the total number of valid subarrays
        prefix_cnt = defaultdict(int)  # Stores remainder frequencies
        prefix_cnt[0] = 1  # Base case: a prefix sum divisible by k initially

        for n in nums:
            prefix_sum += n  # Update running sum
            remain = prefix_sum % k  # Compute remainder when divided by k

            # Adjust negative remainders to always stay positive
            remain = (remain + k) % k

            # If this remainder was seen before, add its frequency to result
            res += prefix_cnt[remain]

            # Increment count of this remainder
            prefix_cnt[remain] += 1

        return res  # Return total count of valid subarrays
```

---

## 3. Approach and Logic Explained

### Prefix Sum + HashMap Approach

We use **prefix sums** and **modulo arithmetic** to solve it efficiently.

#### Key Idea:

* For two prefix sums `prefix[j]` and `prefix[i]` (where `j > i`), the sum of the subarray between them is divisible by `k` if:

  ```
  (prefix[j] - prefix[i]) % k == 0
  ```

  This is equivalent to:

  ```
  prefix[j] % k == prefix[i] % k
  ```
* This means that if two prefix sums have the same remainder when divided by `k`, the subarray between them has a sum divisible by `k`.

#### Algorithm Steps:

1. Initialize a dictionary (`prefix_cnt`) to store how many times each remainder has appeared.
2. Iterate through the array while maintaining a running prefix sum.
3. For each new prefix sum, calculate its remainder when divided by `k`.
4. If this remainder has been seen before, it means there are subarrays ending at this point with a sum divisible by `k`.
5. Increment the remainder count in the dictionary.

#### Why `(remain + k) % k`?

To handle negative numbers properly. In Python, the `%` operator can produce negative results for negative sums, so we adjust it to keep remainders positive.

---

## 4. Time and Space Complexity

### Time Complexity: **O(n)**

* We iterate through the array once, doing constant-time work (mod, addition, dictionary lookup) per element.

### Space Complexity: **O(k)**

* We store at most `k` different remainder values in the hashmap.

### Why This Is Optimal

* The problem inherently depends on prefix sums and modular arithmetic; therefore, we must at least process each element once.
* Using a hash map to count remainders allows us to track subarrays efficiently without recomputing sums.
* Any approach faster than O(n) would be impossible because every element affects the cumulative sum.

---

## 5. Test Cases

```python
# Test Case 1
nums = [4, 5, 0, -2, -3, 1]
k = 5
print(Solution().subarraysDivByK(nums, k))  # Output: 7

# Test Case 2
nums = [5]
k = 9
print(Solution().subarraysDivByK(nums, k))  # Output: 0

# Test Case 3 (negative numbers)
nums = [-1, 2, 9]
k = 2
print(Solution().subarraysDivByK(nums, k))  # Output: 2
```
