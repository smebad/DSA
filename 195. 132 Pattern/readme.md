# 132 Pattern – README - LeetCode

## 1. What is the "132 Pattern" and What is the Problem?

The **132 Pattern problem** is a classic data structure and algorithm question where we are given an integer array `nums`. We must check whether there exists a subsequence of **three** numbers following the order of indices:

```
nums[i] < nums[k] < nums[j]
```

with:

* `i < j < k`
* The values follow the **132 order**: smallest → largest → middle.

This pattern is called **132** because:

* `1` represents the **smallest value** (`nums[i]`)
* `3` represents the **largest value** (`nums[j]`)
* `2` represents the **middle value** (`nums[k]`)

### Example

* Input: `[3, 1, 4, 2]`
* Pattern found: `1 < 2 < 4` → indices `1 < 3 < 2` satisfy the structure.

The task is to return **true** if such a pattern exists; otherwise, **false**.

---

## 2. Explanation of the Code (With Comments)

Below is the given solution with added explanations so you can easily remember how it works.

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # will store pairs [current_value, minimum_value_before_it]
        curMin = nums[0]  # keeps track of the smallest value up to the current index

        for i in range(1, len(nums)):
            # Remove any elements from stack whose first element is <= current nums[i]
            # because they cannot form the "3" part of the 132 pattern anymore.
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()

            # If stack is not empty and current number is greater than the minimum
            # value stored with the top of the stack, it means:
            # curMin < nums[i] < stack[-1][0]
            # This matches the 132 pattern condition.
            if stack and nums[i] > stack[-1][1]:
                return True

            # Push pair: [current number, minimum so far]
            stack.append([nums[i], curMin])

            # Update the running minimum
            curMin = min(curMin, nums[i])

        return False
```

---

## 3. Explanation of the Solution, Approach, and Logic (Beginner Friendly)

### Goal

We want to check if we can find:

```
nums[i] < nums[k] < nums[j]
```

with increasing indices `i < j < k`.

### Main Idea

We use a **stack** to track potential pairs that could serve as:

* the `3` value (`nums[j]`)
* the `1` value (`nums[i]`)

As we iterate through the array, each number (`nums[i]`) becomes a candidate for the `2` part of the pattern.

### Why Track Minimums?

To form a valid `132` pattern:

* The candidate `2` (`nums[k]`) must be greater than a previous minimum.

So we store **for each number**, the minimum value seen before it.

### Why Use a Stack?

The stack helps maintain possible `3` values.
Whenever we see a new number:

* If it is **greater or equal** to the top stack's `3` value, that `3` cannot work anymore and is removed.
* If it fits between a minimum and a bigger number, we found the pattern.

### Summary of the Logic

1. Track the running minimum (`nums[i]`).
2. Use a stack to store combinations of the form `potential_3, min_before_it`.
3. When encountering a new number (`nums[k]`):

   * Remove larger invalid top elements.
   * Check if it fits between the stored min and top element → pattern found.
4. If loop ends without success → no pattern.

### Difference from Brute Force

Brute force would check all combinations of three elements → **O(n³)**.
Even optimized brute force is **O(n²)**.

This stack-based method reduces it to **O(n)**.

---

## 4. Time and Space Complexity

### Time Complexity: **O(n)**

* Each element is pushed to the stack at most once.
* Each element is popped at most once.
* The loop runs once through the array.

Therefore the total work is linear.

### Space Complexity: **O(n)**

* Worst case: the stack stores many elements.

This is acceptable for the constraint of `2 * 10⁵` elements.

### Why This Is Optimal

Theoretical best possible time complexity for scanning a list once is **O(n)**.
Because the problem requires comparing relationships across the array, achieving O(1) or sub-linear time is impossible.

This stack-based solution reaches the optimal limit.

---

## 5. Test Cases
```python
# Test Case 1:
nums1 = [1, 2, 3, 4]
print(Solution().find132pattern(nums1))  # Expected Output: False

# Test Case 2:
nums2 = [3, 1, 4, 2]
print(Solution().find132pattern(nums2))  # Expected Output: True

# Test Case 3:
nums3 = [-1, 3, 2, 0]
print(Solution().find132pattern(nums3))  # Expected Output: True
```