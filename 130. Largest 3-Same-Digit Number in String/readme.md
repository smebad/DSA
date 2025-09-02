# Largest 3-Same-Digit Number in String - LeetCode

## Problem Explanation

The problem **Largest 3-Same-Digit Number in String** asks us to find the largest substring of length 3 in a given numeric string `num` where all three characters are the same digit. Such a substring is called a **good integer**. If no such substring exists, we return an empty string `""`.

### Conditions for a Good Integer:

1. It must be exactly 3 characters long.
2. All three characters must be the same digit.

### Examples

* **Example 1:**

  * Input: `num = "6777133339"`
  * Good integers: `"777"` and `"333"`
  * Largest good integer: `"777"`

* **Example 2:**

  * Input: `num = "2300019"`
  * Good integer: `"000"`
  * Output: `"000"`

* **Example 3:**

  * Input: `num = "42352338"`
  * No good integers exist.
  * Output: `""`

---

## Brute Force Solution

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        val = 0

        # Iterate through the string, checking substrings of length 3
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:  # Found a good integer
                tmp = num[i : i + 3]
                if val <= int(tmp):  # Compare with current maximum
                    val = int(tmp)
                    res = tmp

        return res
```

### Explanation of Code

* We loop through the string and check every substring of length 3.
* If all three characters are the same, we store it as a temporary good integer.
* We compare it with the previously found maximum good integer and update if needed.
* At the end, we return the largest good integer.

### Complexity

* **Time Complexity:** `O(n)` where `n` is the length of the string, since we scan through once.
* **Space Complexity:** `O(1)` since only constant extra space is used.

---

## Iteration Solution

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = "0"  # Start with smallest possible value

        # Iterate through the string, checking substrings of length 3
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:  # Found a good integer
                res = max(res, num[i : i + 3])  # Keep the maximum one

        return "" if res == "0" else res
```

### Explanation of Code

* Instead of tracking integer values separately, we directly compare substrings using `max`.
* This simplifies the code because string comparison works lexicographically, which is valid for equal-length numeric substrings.
* If no valid good integer is found, we return an empty string.

### Complexity

* **Time Complexity:** `O(n)` where `n` is the length of the string.
* **Space Complexity:** `O(1)` since only constant extra space is used.

---

## Approach and Differences

* Both solutions scan the string once and check for substrings of length 3.
* **Brute Force Solution:** Uses an integer variable to track the largest value found.
* **Iteration Solution:** Uses direct string comparison with `max`, making it shorter and cleaner.

Both are equally efficient in time and space. The **iteration solution is considered more optimal in practice** because:

1. It avoids unnecessary integer conversions (`int(tmp)`).
2. It leverages Python’s built-in string comparison for simplicity.

---

## Final Analysis

* **Best Approach:** Iteration solution.
* **Reason:** Same time and space complexity as brute force but less overhead and cleaner code.
* **Time Complexity:** `O(n)` for both.
* **Space Complexity:** `O(1)` for both.

Thus, the iteration solution is the most optimal one due to its simplicity and direct use of built-in operations.
