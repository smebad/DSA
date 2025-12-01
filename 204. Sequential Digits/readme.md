# Sequential Digits - LeetCode

## 1. Problem Explanation

The **Sequential Digits** problem asks us to find all numbers within a given range ([low, high]) such that every digit in the number is exactly one greater than the previous digit.

For example:

* 123 is valid because 2 comes after 1 and 3 comes after 2.
* 789 is valid.
* 124 is not valid because 4 does not directly follow 2.

We must return all such numbers in **sorted order** that lie between `low` and `high` (inclusive).

---

## 2. Brute Force Code With Comments

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []  # This list will store all valid sequential digit numbers

        # Loop through every number from low to high
        for num in range(low, high + 1):
            s = str(num)  # Convert number to string to check digits easily
            flag = True  # Assume it is sequential until proven otherwise

            # Compare each digit with the previous one
            for i in range(1, len(s)):
                # If current digit is not exactly 1 greater than previous
                if ord(s[i]) - ord(s[i - 1]) != 1:
                    flag = False
                    break

            # If the number remained sequential, add it to result
            if flag:
                res.append(num)

        return res
```

### What This Code Does

* It checks **every number** from `low` to `high`.
* Converts each number into a string.
* Compares each digit with the previous one.
* If all digits increase by exactly 1, the number is added to the result list.

---

## 3. Queue-Based Solution With Comments

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []  # Stores valid sequential numbers
        queue = deque(range(1, 10))  # Start with digits 1 to 9

        while queue:
            n = queue.popleft()  # Take a number from the queue

            if n > high:
                continue  # Stop processing this number if too large

            if low <= n <= high:
                res.append(n)  # Valid sequential number within range

            ones = n % 10  # Get the last digit

            if ones < 9:
                queue.append(n * 10 + (ones + 1))  # Build next sequential number

        return res
```

### What This Code Does

* It **generates only sequential numbers**, instead of checking every number.
* Starts with digits 1 to 9.
* Repeatedly builds new sequential numbers by adding the next digit.
* Adds only valid numbers inside `[low, high]` to the result.

---

## 4. Solution Approach and Logic
### Brute Force Approach

* Go through every number in the range.
* Check each number digit-by-digit.
* Keep only those that increase by exactly 1 every step.

**Problem:**
This is slow when `low` and `high` are far apart because you check millions of numbers.

---

### Queue-Based Approach

* Instead of checking every number, **directly generate only sequential numbers**.
* Start from 1 to 9.
* Keep appending the next increasing digit.
* Stop when numbers exceed `high`.

**Why It Is Better:**

* There are only **36 possible sequential digit numbers** within the entire constraint.
* You avoid unnecessary looping.

---

## 5. Difference Between the Two Solutions

| Brute Force                     | Queue-Based                             |
| ------------------------------- | --------------------------------------- |
| Checks all numbers in the range | Generates only valid sequential numbers |
| Very slow for large ranges      | Extremely fast                          |
| Simple to understand            | Slightly more advanced                  |
| Time depends on `high - low`    | Constant time                           |

---

## 6. Time and Space Complexity Analysis

### Brute Force Solution

* **Time Complexity:** O(high − low)
* **Space Complexity:** O(1)
* **Why It Is Slow:** It checks every number in the range.

---

### Queue-Based Solution (Most Optimal)

* **Time Complexity:** O(1)
* **Space Complexity:** O(1)
* **Why It Is Optimal:**

  * Only a fixed number of sequential digit values exist.
  * The algorithm never depends on the size of the input range.
  * It directly builds only valid numbers.

---

## 7. Test Cases
```python
sol = Solution()
# Test Case 1:
low1 = 100
high1 = 300
print(sol.sequentialDigits(low1, high1))  # Output: [123, 234]

# Test Case 2:
low2 = 1000
high2 = 13000
print(sol.sequentialDigits(low2, high2))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]
```