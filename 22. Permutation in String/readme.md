# Permutation in String - LeetCode

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

### Examples:

**Example 1:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

### Constraints:
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

---

## Brute Force Solution (Using Hash Map)

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
```

### Explanation:
1. Count frequencies of characters in `s1` and store in `count1`.
2. Iterate through `s2` using a nested loop to build substrings.
3. Track the frequency of characters in the current substring and compare to `count1`.
4. If the number of matched character frequencies equals the number of unique characters in `s1`, return `True`.
5. Otherwise, continue the search.

### Time Complexity:
- **O(n * m)** where `n` is the length of `s2` and `m` is the length of `s1`.
- Nested loop results in higher runtime for large inputs.

### Space Complexity:
- **O(1)** since the character count is limited to 26 lowercase English letters.

This solution is not optimal for large input sizes.

---

## Optimal Solution (Sliding Window with Frequency Count)

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add new character to the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the old character from the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26
```

### Explanation:
1. Initialize frequency arrays of size 26 for both `s1` and the current window in `s2`.
2. Populate the counts for the first window of `s2`.
3. Count how many characters match in both arrays.
4. Slide the window one character at a time:
   - Add the new character to the window.
   - Remove the leftmost character.
   - Adjust the match counter based on how the frequency changes.
5. If all 26 character frequencies match, return `True`.

### Time Complexity:
- **O(n)** where `n` is the length of `s2`.
- Only one pass through `s2` with constant time operations per character.

### Space Complexity:
- **O(1)**: Fixed size frequency arrays of length 26.

This is the most efficient and optimal solution to the problem.

---

## Test Cases
```python
# Test Case 1
print(Solution().checkInclusion('ab', 'eidbaooo'))  # True

# Test Case 2
print(Solution().checkInclusion('ab', 'eidboaoo'))  # False
```

---

## Summary
- The brute force approach builds substring counts each time, which is slow.
- The sliding window approach uses fixed size arrays and matches frequencies in `O(n)` time.
- Optimal approach is preferred for solving this problem efficiently, especially for large input sizes.