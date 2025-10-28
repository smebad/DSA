# Subarray Product Less Than K - LeetCode

## Problem Description

The problem **"Subarray Product Less Than K"** asks us to find the number of contiguous subarrays in a given integer array `nums` where the product of all elements in the subarray is **strictly less than a given integer `k`**.

A **subarray** is defined as a contiguous portion of the array.

### Example 1

**Input:** `nums = [10, 5, 2, 6]`, `k = 100`
**Output:** `8`

**Explanation:** The 8 subarrays where the product is less than 100 are:
`[10]`, `[5]`, `[2]`, `[6]`, `[10, 5]`, `[5, 2]`, `[2, 6]`, `[5, 2, 6]`

Note that `[10, 5, 2]` is **not** included because its product equals 100, which is not less than `k`.

### Example 2

**Input:** `nums = [1, 2, 3]`, `k = 0`
**Output:** `0`

If `k` is 0 or 1, no positive product can ever be strictly less than `k`, hence the answer is `0`.

### Constraints

* `1 <= nums.length <= 3 * 10^4`
* `1 <= nums[i] <= 1000`
* `0 <= k <= 10^6`

---

## Code Implementation (Sliding Window Solution)

```python
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0  # Stores total count of valid subarrays
        l = 0    # Left pointer for sliding window
        product = 1  # Current product of window elements
        
        for r in range(len(nums)):  # Right pointer expands the window
            product *= nums[r]
            
            # If product exceeds or equals k, shrink window from left
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
                
            # The number of valid subarrays ending at index r
            # equals the window size (r - l + 1)
            res += (r - l + 1)
        
        return res
```

---

## Step-by-Step Logic and Approach

### 1. **Why Sliding Window?**

The key idea is that when the product of a subarray becomes too large (≥ k), extending it further will only increase the product. So, we can use a **sliding window** to maintain a valid range of elements whose product remains below `k`.

### 2. **How It Works:**

* We maintain two pointers `l` (left) and `r` (right) to represent the current window.
* Multiply `nums[r]` to the `product` as we expand the window.
* If `product` becomes **greater than or equal to `k`**, move the left pointer `l` forward and divide the product by `nums[l]` until the condition is restored.
* Every time the condition `product < k` is true, all subarrays ending at `r` and starting anywhere from `l` to `r` are valid. The count of such subarrays is `(r - l + 1)`.

### 3. **Example Walkthrough:**

Let `nums = [10, 5, 2, 6]`, `k = 100`.

| Step | r | nums[r] | product | Action                             | l | Count Added | Total |
| ---- | - | ------- | ------- | ---------------------------------- | - | ----------- | ----- |
| 1    | 0 | 10      | 10      | product < k                        | 0 | 1           | 1     |
| 2    | 1 | 5       | 50      | product < k                        | 0 | 2           | 3     |
| 3    | 2 | 2       | 100     | product >= k, divide by nums[l]=10 | 1 | 2           | 5     |
| 4    | 3 | 6       | 60      | product < k                        | 1 | 3           | 8     |

Result = **8**

---

## Time and Space Complexity

### **Time Complexity:** `O(n)`

* Each element is visited at most twice — once when added to the window (by the right pointer) and once when removed (by the left pointer).
* Hence, the algorithm runs in linear time relative to the array size.

### **Space Complexity:** `O(1)`

* We only use a few variables (`res`, `l`, `product`), so the space usage is constant regardless of the input size.

---

## Why This is the Most Optimal Solution

* A brute force approach would check all possible subarrays and calculate their products, taking **O(n²)** time — inefficient for large arrays.
* The **sliding window technique** intelligently adjusts the boundaries to maintain the valid condition, achieving **O(n)** efficiency.
* Therefore, this approach is **optimal** in both **time** and **space**.

---

## Test Cases

```python
solution = Solution()

# Test Case 1
nums1 = [10, 5, 2, 6]
k1 = 100
print(solution.numSubarrayProductLessThanK(nums1, k1))  # Expected Output: 8

# Test Case 2
nums2 = [1, 2, 3]
k2 = 0
print(solution.numSubarrayProductLessThanK(nums2, k2))  # Expected Output: 0
```