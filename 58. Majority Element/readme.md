# Majority Element - LeetCode

## Problem Statement

Given an array `nums` of size `n`, return the majority element.

The **majority element** is the element that appears **more than** $\lfloor n / 2 \rfloor$ times. You may assume that the majority element always exists in the array.

---

## Examples

### Example 1:

```
Input: nums = [3, 2, 3]  
Output: 3
```

### Example 2:

```
Input: nums = [2, 2, 1, 1, 1, 2, 2]  
Output: 2
```

---

## Constraints

* `n == nums.length`
* `1 <= n <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

---

## Follow-Up

Can you solve the problem in **linear time** and **O(1) space**?

---

## What is a Majority Element?

A **majority element** is a number that appears **more than half** the number of times in a given list. For example, if the list has 7 elements, the majority element must appear more than 3 times. It is guaranteed that such an element exists.

---

## Solution 1: Hash Map (Frequency Count)

```python
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)  # Dictionary to store the frequency of each number
        res = maxCount = 0        # res holds the majority element, maxCount tracks highest frequency

        for num in nums:
            count[num] += 1           # Increase count of current number
            if maxCount < count[num]:
                res = num            # Update result if current number's count is greater
                maxCount = count[num]
        return res
```

### Explanation:

* We loop through the list and count how many times each number appears using a dictionary.
* If any number's count exceeds the current `maxCount`, we update our result.

### Time Complexity: `O(n)`

* We loop through the list once.

### Space Complexity: `O(n)`

* We may store all elements in the dictionary.

### Pros:

* Easy to understand.
* Works efficiently for all input sizes.

### Cons:

* Uses extra space.

---

## Solution 2: Sorting

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()                      # Sorts the array
        return nums[len(nums) // 2]     # The middle element will be the majority one
```

### Explanation:

* After sorting, the majority element will always be at the middle index, since it appears more than half the time.

### Time Complexity: `O(n log n)`

* Sorting takes `n log n` time.

### Space Complexity: `O(1)`

* Sorting is in-place; no extra data structures are used.

### Pros:

* Simple and short.

### Cons:

* Not optimal for large lists due to sorting time.

---

## Solution 3: Brute Force

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)  # Count occurrences of num
            if count > n // 2:
                return num
```

### Explanation:

* For each number, count how many times it appears.
* If it appears more than half the length of the list, return it.

### Time Complexity: `O(n^2)`

* For each number, we loop through the list again.

### Space Complexity: `O(1)`

* No additional space used.

### Pros:

* Simple to understand.

### Cons:

* Very slow for large inputs.

---

## Which One is Optimal?

Among all the above methods, the **Hash Map** solution is the best trade-off between time and simplicity. However, it does not meet the follow-up requirement of `O(1)` space.

To fully meet the follow-up (linear time and constant space), the **Boyer-Moore Voting Algorithm** is the most optimal. It works by maintaining a count and a candidate and iterating once through the array.

But from the solutions provided above:

* **Most Optimal:** Hash Map
* **Why Optimal?**

  * Time: O(n)
  * Simplicity: Easy to understand
  * Works well for all valid input sizes

If space is a concern and time is flexible, the **Sorting** solution is a good fallback.

---

## Summary of Approaches

| Approach    | Time Complexity | Space Complexity | In-place | Optimal? |
| ----------- | --------------- | ---------------- | -------- | -------- |
| Hash Map    | O(n)            | O(n)             | No       | Yes      |
| Sorting     | O(n log n)      | O(1)             | Yes      | No       |
| Brute Force | O(n^2)          | O(1)             | Yes      | No       |

---
