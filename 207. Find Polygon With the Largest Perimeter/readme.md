# Find Polygon With the Largest Perimeter - LeetCode

## 1. Problem Explanation

The problem **"Find Polygon With the Largest Perimeter"** asks us to determine the **maximum possible perimeter of a polygon** that can be formed using some or all values from a given array of positive integers.

Rules for forming a valid polygon:

* A polygon must have **at least 3 sides**.
* The **longest side must be smaller than the sum of the other sides**.
* The perimeter is the **sum of all side lengths used**.
* If it is impossible to form any valid polygon, return **-1**.

In simple words, we must select some numbers from the array such that:

1. There are at least three sides.
2. The largest side is strictly **less than the sum of the remaining sides**.
3. The sum of those selected sides is as **large as possible**.

---

## 2. Code With Comments

```python
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in non-decreasing order
        nums.sort()
        
        # This will store the best (largest) valid perimeter found so far
        res = -1
        
        # This will store the sum of all previous numbers as we iterate
        total = 0
        
        for num in nums:
            # If the sum of all previous sides is greater than
            # the current side, then a valid polygon can be formed
            if total > num:
                # Update the result with the new larger perimeter
                res = total + num
            
            # Add the current number to total for future checks
            total += num
        
        # If no valid polygon was found, this will remain -1
        return res
```

---

## 3. Solution Approach, Logic, and Explanation

### Step-by-Step Logic

1. **Sort the array**:

   * Sorting helps us ensure that when we check the polygon condition, the **current number is the largest side**.
   * This makes the polygon condition easy to verify.

2. **Use a running sum (`total`)**:

   * As we move through the sorted array, we keep adding previous elements into `total`.

3. **Apply the polygon rule**:

   * For a valid polygon, we must check:

     **Sum of previous sides > current side**

     That means:

     `total > num`

4. **Update the perimeter**:

   * If the condition is satisfied, we update:

     `res = total + num`
   * This ensures we always keep the largest possible perimeter.

5. **Return result**:

   * If no valid polygon is found, `res` remains `-1`.

---

### Why This Works

* Because the list is sorted, when we reach a number, it is the **largest side so far**.
* If the sum of all previous sides is greater than this number, then a polygon can definitely be formed using all those sides.
* By moving forward and continuously checking, we **maximize the perimeter naturally**.

---

## 4. Time and Space Complexity Analysis

### Time Complexity

* **Sorting:** `O(n log n)`
* **Single loop through array:** `O(n)`

Final Time Complexity:

`O(n log n)`

---

### Space Complexity

* No extra data structures are used apart from a few variables.
* Space used is constant.

Final Space Complexity:

`O(1)` (ignoring the input array itself)

---

## 5. Why This Solution Is Optimal

* Sorting is necessary because the polygon condition depends on comparing the **largest side** with the sum of the others.
* Without sorting, checking every possible subset would be computationally expensive.
* This solution performs only:

  * One sort
  * One pass over the array
* This results in the **lowest possible time complexity** for a guaranteed correct solution.

---

## 6. Example Walkthrough

Example:

```python
nums = [1,12,1,2,5,50,3]
```

After sorting:

```
[1, 1, 2, 3, 5, 12, 50]
```

We gradually build `total`:

* total = 1
* total = 2
* total = 4
* total = 7
* total = 12 (valid polygon -> perimeter = 12)
* 12 ≤ 50 → invalid

Final Answer:

```
12
```

---

## 7. Test Cases

```python
# Test Case 1
nums = [5,5,5]
print(sol.largestPerimeter(nums))  # Output: 15

# Test Case 2
nums = [1,12,1,2,5,50,3]
print(sol.largestPerimeter(nums))  # Output: 12

# Test Case 3
nums = [5,5,50]
print(sol.largestPerimeter(nums))  # Output: -1
```