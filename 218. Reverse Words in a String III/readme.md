# Reverse Words in a String III - LeetCode

## 1. Problem Explanation

The problem **Reverse Words in a String III** asks us to reverse the characters of each word in a sentence while keeping:

* The original word order
* The original spacing between words

A *word* is defined as a sequence of characters separated by a single space.

You are given a string `s`, and your task is to return a new string where **each individual word is reversed**, but the sentence structure remains the same.

### Example

Input:

```
"Let's take LeetCode contest"
```

Output:

```
"s'teL ekat edoCteeL tsetnoc"
```

Only the characters inside each word are reversed. The spaces stay in the same positions.

---

## 2. Code Explanation (With Comments)

Below is the exact solution you provided, with added comments to help remember how and why it works.

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert string to list because Python strings are immutable
        s = list(s)

        # l marks the start index of the current word
        l = 0

        # r moves through the string character by character
        for r in range(len(s)):
            # When we find a space or reach the end of the string
            if s[r] == " " or r == len(s) - 1:
                # Determine the end index of the current word
                temp_l = l
                temp_r = r - 1 if s[r] == " " else r

                # Reverse the characters of the current word
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1

                # Move l to the start of the next word
                l = r + 1

        # Convert the list back to a string
        return "".join(s)
```

---

## 3. Solution Approach and Logic

### Core Idea

The main idea is:

* Scan the string from left to right
* Detect each word using spaces as separators
* Reverse each word **in place** using two pointers

### Step-by-Step Logic

1. Convert the string into a list so characters can be swapped.
2. Use pointer `l` to mark the start of a word.
3. Move pointer `r` across the string.
4. When a space or the end of the string is found:

   * Reverse the word between `l` and `r - 1` (or `r` if at the end).
5. Update `l` to start tracking the next word.
6. After processing all words, convert the list back to a string.

### Why Two Pointers?

Using two pointers allows:

* Reversing characters without creating extra strings
* Efficient in-place swaps
* Clear control over word boundaries

### Alternative Approach (Conceptual)

A simpler approach could be:

* Split the string by spaces
* Reverse each word using slicing
* Join the words back with spaces

However, that approach uses extra memory for split strings and intermediate lists.

Your two-pointer approach avoids unnecessary string operations and is more optimal.

---

## 4. Time and Space Complexity

### Time Complexity

* **O(n)**, where `n` is the length of the string
* Each character is visited a constant number of times

### Space Complexity

* **O(n)** for converting the string into a list
* The actual reversing process uses **O(1)** extra space

### Most Optimal Solution

This two-pointer solution is optimal because:

* It processes the string in one pass
* It avoids repeated string slicing
* It performs in-place character swaps
* It works efficiently within the given constraints

For large strings, this approach is faster and more memory-efficient than rebuilding strings repeatedly.

---

## 5. Test Cases
```python
solution = Solution()
# Test Case 1:
s1 = "Let's take LeetCode contest"
print(solution.reverseWords(s1))  # Output: "s'teL ekat edoCteeL tsetnoc"

# Test Case 2:
s2 = "Mr Ding"
print(solution.reverseWords(s2))  # Output: "rM gniD"

# Test Case 3:
s3 = "My name is Ebad"
print(solution.reverseWords(s3))  # Output: "yM eman si dabe"
```