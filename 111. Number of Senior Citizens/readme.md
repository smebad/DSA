# Number of Senior Citizens - LeetCode

## Problem Description

You are given a 0-indexed array of strings `details`. Each string has exactly 15 characters that encode a passenger's information:

* The **first 10 characters** represent the passenger's phone number.
* The **11th character** represents the gender ('M', 'F', or 'O').
* The **12th and 13th characters** represent the **age** of the passenger (two digits).
* The **last 2 characters** represent the seat number.

Your task is to return the number of passengers who are **strictly older than 60**.

### Example 1

```python
Input: ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
Output: 2
Explanation: Ages are 75, 92, and 40. Two passengers are above 60.
```

### Example 2

```python
Input: ["1313579440F2036", "2921522980M5644"]
Output: 0
Explanation: No passenger is older than 60.
```

### Constraints

* 1 <= details.length <= 100
* details\[i].length == 15
* details\[i] consists of digits and exactly one gender character at index 10.
* The phone numbers and seat numbers are unique.

---

## Solution 1: String Parsing

```python
from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            # Extract age by slicing characters at index 11 and 12
            if int(d[11:13]) > 60:
                res += 1
        return res
```

### Code Explanation

* Iterate over each passenger's details.
* Use string slicing (`d[11:13]`) to extract the age as a string.
* Convert the age string to an integer and compare it with 60.
* If greater than 60, increment the result.

---

## Solution 2: Character-Based Arithmetic

```python
from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            # Convert individual characters to digits manually
            ten = ord(d[11]) - ord("0")  # Tens place
            one = ord(d[12]) - ord("0")  # Ones place
            age = one + 10 * ten
            if age > 60:
                res += 1
        return res
```

### Code Explanation

* Manually convert the characters at positions 11 and 12 to digits.
* Construct the age by computing `10 * tens + ones`.
* Compare the age to 60 and increment the counter accordingly.

---

## Approach Comparison

| Approach             | Technique              | Pros                           | Cons                        |
| -------------------- | ---------------------- | ------------------------------ | --------------------------- |
| String Parsing       | `int(d[11:13])`        | Simple and readable            | Slightly more memory        |
| Character Arithmetic | `ord(d[i]) - ord('0')` | Slightly faster in tight loops | Less readable for beginners |

Both approaches achieve the same result with similar efficiency. The character-based solution avoids slicing and conversions, making it very slightly faster in large-scale applications.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`, where `n` is the number of entries in the `details` list. Each entry is processed in constant time.
* **Space Complexity:** `O(1)`, only a counter is used regardless of input size.

---

## Optimality

Both solutions are optimal:

* They require only one pass over the data.
* No extra space is used beyond a single result variable.
* Processing is done in-place using string indexing or arithmetic.

---

## Test Cases

```python
# Test Case 1
print(Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))  # Output: 2

# Test Case 2
print(Solution().countSeniors(["1313579440F2036", "2921522980M5644"]))  # Output: 0
```