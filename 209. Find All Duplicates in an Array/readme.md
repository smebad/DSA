# Find All Duplicates in an Array - LeetCode

## 1. Problem Explanation

You are given an integer array `nums` of length `n` where:

* Each number lies in the range `[1, n]`
* Every number appears either once or twice

Your task is to return all numbers that appear **exactly twice** in the array.

### Important Conditions

* The solution must run in **O(n) time**
* The solution must use **constant auxiliary space** (excluding output storage)

This problem is important because it tests your understanding of:

* In-place array manipulation
* Index mapping
* Time and space optimization

---

## 2. Code With Line-by-Line Comments

### Negative Marking Solution (Optimal)

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []  # This list will store all duplicate numbers

        for num in nums:
            # Use absolute value because some elements may have been negated already
            idx = abs(num) - 1  # Convert value to index

            # If the number at this index is already negative,
            # it means we've seen this number before
            if nums[idx] < 0:
                res.append(abs(num))

            # Mark this index as visited by making it negative
            nums[idx] = -nums[idx]

        return res
```

---

### Sorting Solution

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sort the array first
        res = []

        # Compare adjacent elements to find duplicates
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])

        return res
```

---

### Hashmap Solution

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)  # Count frequency of each number
        res = []

        # If a number appears twice, add it to the result
        for num in count:
            if count[num] == 2:
                res.append(num)

        return res
```

---

## 3. Detailed Explanation of All Approaches

### Negative Marking Approach

Idea:

* Since all numbers are between `1` and `n`, each number maps directly to an index.
* For each number `x`, go to index `x-1`.
* If the value at that index is positive, make it negative to mark it visited.
* If it is already negative, that means the number has appeared before.

Why it works:

* The array itself is used as a visited tracker.
* No extra memory is required.

Example:
Input: `[4,3,2,7,8,2,3,1]`

* First time you visit 2, you mark its index negative
* Second time you visit 2, its index is already negative, so 2 is a duplicate

---

### Sorting Approach

Idea:

* If the array is sorted, duplicate numbers will become adjacent.
* Simply check every adjacent pair.

Steps:

1. Sort the array
2. Compare `nums[i]` and `nums[i+1]`
3. If equal, it is a duplicate

Why it is slower:

* Sorting alone takes `O(n log n)` time

---

### Hashmap Approach

Idea:

* Count how many times each number appears.
* Add numbers to the result if their count is 2.

Why it is simple:

* Very easy to write and understand

Why it is not optimal:

* Uses extra memory for the hashmap

---

### Differences Between the Solutions

| Solution Type    | Time       | Space | Modifies Input | Optimal |
| ---------------- | ---------- | ----- | -------------- | ------- |
| Negative Marking | O(n)       | O(1)  | Yes            | Yes     |
| Sorting          | O(n log n) | O(1)  | Yes            | No      |
| Hashmap          | O(n)       | O(n)  | No             | No      |

---

## 4. Time and Space Complexity Analysis

### Negative Marking Solution (Best Solution)

* Time Complexity: `O(n)`
* Space Complexity: `O(1)` (excluding result list)

Why it is optimal:

* It runs in linear time
* Uses no extra memory
* Fully satisfies the problem constraints

---

### Sorting Solution

* Time Complexity: `O(n log n)`
* Space Complexity: `O(1)`

Not optimal because:

* Sorting increases time complexity

---

### Hashmap Solution

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

Not optimal because:

* Extra memory is required

---

## Final Conclusion

The **Negative Marking Solution** is the most efficient and optimal approach for this problem because it:

* Runs in the fastest possible time
* Uses constant auxiliary space
* Fully satisfies the problem constraints

The sorting and hashmap solutions are useful for understanding the problem but do not meet the strict optimization requirements.

---

## 5. Test Cases
```python
solution = Solution()

# Test Case 1
nums1 = [4,3,2,7,8,2,3,1]
print(solution.findDuplicates(nums1))  # Expected output: [2, 3]

# Test Case 2
nums2 = [1,1,2]
print(solution.findDuplicates(nums2))  # Expected output: [1]

# Test Case 3
nums3 = [1]
print(solution.findDuplicates(nums3))  # Expected output: []
```