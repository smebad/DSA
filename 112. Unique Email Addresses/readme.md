# Unique Email Addresses - LeetCode

## Problem Description

In this problem, we are given a list of email addresses. Each email consists of two parts:

* **Local name** (before `@`)
* **Domain name** (after `@`)

Certain rules apply to the local name:

* Dots `.` in the local name are ignored.
* Everything after a plus `+` in the local name is ignored.

These rules **do not** apply to the domain name.

### Objective

Return the number of **unique** email addresses that will actually receive the emails.

---

## Built-in Functions Solution

```python
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()  # Set to store unique cleaned emails

        for e in emails:
            local, domain = e.split('@')  # Split into local and domain part
            local = local.split("+")[0]  # Ignore everything after '+' in local part
            local = local.replace(".", "")  # Remove all dots from local part
            unique.add((local, domain))  # Add cleaned email to set

        return len(unique)  # Return count of unique emails
```

---

## Iteration-Based Solution

```python
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()  # Set to store unique emails

        for e in emails:
            i, local = 0, ""
            # Build local part until '+' or '@'
            while e[i] not in ["@", "+"]:
                if e[i] != ".":  # Ignore dots
                    local += e[i]
                i += 1

            # Skip remaining characters until '@' if '+' encountered
            while e[i] != "@":
                i += 1
            domain = e[i + 1:]  # Get domain part

            unique.add((local, domain))  # Store the cleaned version in the set

        return len(unique)  # Return number of unique emails
```

---

## Solution Approach & Explanation

Both solutions solve the same problem using slightly different techniques:

### **1. Built-in Functions Approach:**

* Splits the email into local and domain using `split('@')`.
* Truncates everything after the `+` in the local part.
* Removes all `.` characters from the local part.
* Combines the cleaned local part with domain to create the normalized email.
* Adds it to a set to ensure uniqueness.

### **2. Iteration-Based Approach:**

* Manually constructs the local name by iterating through each character.
* Ignores `.` and stops processing at `+`.
* Skips characters until it finds `@` to get the domain name.
* Constructs the cleaned email and stores it in a set.

### Key Differences:

* The first approach uses Python's built-in string manipulation functions (like `split()` and `replace()`), making it more readable and concise.
* The second approach avoids using built-in functions and does the parsing manually using loops and conditions. It's more verbose but useful for understanding how string processing works at a lower level.

---

## Time and Space Complexity

### **Time Complexity:**

* **O(n \* m)** for both solutions, where:

  * `n` = number of emails
  * `m` = average length of each email
* Each email is processed once, and each character may be examined individually.

### **Space Complexity:**

* **O(n)** in the worst case, where all emails are unique and stored in the set.

---

## Most Optimal Solution

The **built-in functions approach** is considered optimal here because:

* It is simpler and easier to read and maintain.
* It avoids manual character-by-character processing.
* It achieves the same efficiency (O(n \* m) time) as the manual iteration approach.

There is no need for additional data structures beyond the set used to store unique results, making the space usage efficient.

---

## Example

### Input:

```python
emails = [
  "test.email+alex@leetcode.com",
  "test.e.mail+bob.cathy@leetcode.com",
  "testemail+david@lee.tcode.com"
]
```

### Output:

```
2
```

### Explanation:

* All variations of `test.email+alex@leetcode.com` normalize to `testemail@leetcode.com`
* The third email normalizes to `testemail@lee.tcode.com`
* Hence, only **2 unique addresses** actually receive emails.

---

## Conclusion

This problem teaches string processing, parsing, and the use of sets for tracking unique values. Both solutions are efficient, but the built-in function version is typically preferred in production code due to its readability and maintainability.