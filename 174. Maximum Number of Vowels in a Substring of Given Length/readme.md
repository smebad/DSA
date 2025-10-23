# Maximum Number of Vowels in a Substring of Given Length - LeetCode

## Problem Explanation

The **"Maximum Number of Vowels in a Substring of Given Length"** problem asks you to find the largest number of vowel letters ('a', 'e', 'i', 'o', 'u') that appear in any substring of length `k` within a given string `s`.

In other words, you must slide a window of length `k` across the string and find the maximum number of vowels present in any window.

### Example

**Input:** `s = "abciiidef"`, `k = 3`
**Output:** `3`
**Explanation:** The substring "iii" contains 3 vowels, which is the highest possible count for a substring of length 3.

---

## Code Explanation

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels for quick lookup

        l = cnt = res = 0  # Initialize left pointer, current vowel count, and max result
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0  # Add 1 if the current character is a vowel

            # If window size exceeds k, remove the leftmost character's contribution
            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1  # Move the left pointer forward

            # Update maximum vowels found so far
            res = max(res, cnt)
        return res
```

---

## Approach and Logic

### Sliding Window Technique

1. **Initialize two pointers (`l` and `r`)** to represent a sliding window over the string.
2. **Maintain a counter `cnt`** that keeps track of how many vowels are currently inside the window.
3. As the right pointer `r` moves forward:

   * Add 1 to the count if `s[r]` is a vowel.
   * If the window exceeds size `k`, subtract 1 if `s[l]` (the leftmost character) is a vowel, and move the left pointer forward.
4. **Update the maximum count** (`res`) after every iteration.
5. Continue until the end of the string, and return `res` as the maximum number of vowels found in any substring of length `k`.

### Key Idea

* Instead of checking every possible substring separately (which would take O(n*k) time), the **sliding window** allows us to reuse the count from the previous window by just adding and removing one character at a time.
* This makes the algorithm very efficient.

---

## Complexity Analysis

* **Time Complexity:** O(n), where `n` is the length of the string `s`. Each character is visited once by the right pointer and at most once by the left pointer.
* **Space Complexity:** O(1), since we use only a few variables and a fixed-size vowel set.

---

## Why This Solution is Optimal

This approach is optimal because:

* We only traverse the string once using two pointers.
* Each operation inside the loop (vowel check, increment/decrement) takes constant time.
* No additional data structures that scale with input size are used.

Thus, the sliding window method achieves the best possible efficiency for this problem.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
s1 = "abciiidef"
k1 = 3
print(sol.maxVowels(s1, k1))  # Expected Output: 3

# Test Case 2
s2 = "aeiou"
k2 = 2
print(sol.maxVowels(s2, k2))  # Expected Output: 2

# Test Case 3
s3 = "leetcode"
k3 = 3
print(sol.maxVowels(s3, k3))  # Expected Output: 2
```