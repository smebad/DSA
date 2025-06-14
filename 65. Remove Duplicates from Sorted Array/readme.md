# Remove Duplicates from Sorted Array - LeetCode

## Problem Description

The **Remove Duplicates from Sorted Array** problem requires removing duplicate values from a given sorted array `nums` in-place. The goal is to ensure that each unique element appears only once and to return the number of such unique elements. The relative order of the elements should be maintained.

You're required to do this **without using extra space** — meaning the operation must modify the original array `nums` directly.

### Example 1:

* **Input:** `nums = [1,1,2]`
* **Output:** `2`, `nums = [1,2,_]`
* **Explanation:** The function returns `2` because there are two unique elements: `1` and `2`. The rest of the array is not important.

### Example 2:

* **Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`
* **Output:** `5`, `nums = [0,1,2,3,4,_,_,_,_,_]`
* **Explanation:** The function returns `5` because there are five unique elements.

## Constraints

* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`
* The input array `nums` is sorted in non-decreasing order.

---

## Solution 1: Two Pointers (Optimal and In-Place)

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1  # Pointer to place the next unique value
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:  # Compare current and previous elements
                nums[l] = nums[r]      # Place unique value at the l-th position
                l += 1                 # Move the left pointer forward
        return l  # l will be the count of unique elements
```

### Explanation

* We use two pointers: `r` (reader) scans the array and `l` (writer) updates the array with unique values.
* When `nums[r]` is different from the previous value `nums[r-1]`, it's a unique number.
* This unique number is written at index `l` and we increment `l`.
* At the end, `l` gives us the count of unique elements.

### Time and Space Complexity

* **Time Complexity:** `O(n)` — We go through the array once.
* **Space Complexity:** `O(1)` — We use only a few extra variables.

### Why It Is Optimal

* It solves the problem in a single pass.
* It uses no extra memory.
* It modifies the array in-place.

---

## Solution 2: Using `set()` and Sorting (Less Optimal)

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))          # Remove duplicates and sort again
        nums[:len(unique)] = unique         # Copy back to original array
        return len(unique)                  # Return the number of unique elements
```

### Explanation

* Convert the array to a set to remove duplicates.
* Sort the resulting set to maintain the order.
* Replace the first `k` elements of `nums` with the sorted unique elements.

### Time and Space Complexity

* **Time Complexity:** `O(n log n)` — Due to sorting.
* **Space Complexity:** `O(n)` — We create a new set and list.

### When to Use

* This method is easier to implement but is less efficient for large arrays.
* It is **not in-place**, technically, due to extra memory usage.

---

## Summary of Differences

| Feature          | Two Pointers            | Sorted Set Method     |
| ---------------- | ----------------------- | --------------------- |
| Time Complexity  | `O(n)`                  | `O(n log n)`          |
| Space Complexity | `O(1)`                  | `O(n)`                |
| In-Place         | Yes                     | No                    |
| Efficiency       | High                    | Moderate              |
| Simplicity       | Medium (requires logic) | High (uses built-ins) |

---

## Test Cases

```python
# Test Case 1
nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))  # Output: 2

# Test Case 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))  # Output: 5

# Test Case 3
nums = [1,2,3,4,5]
print(Solution().removeDuplicates(nums))  # Output: 5
```
