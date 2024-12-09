# Compress Problem

## Overview

The **Compress** problem involves compressing a given string by replacing consecutive occurrences of the same character with the count of those occurrences followed by the character itself. For characters that appear only once, no compression is applied.

### Examples:
- `'aaa'` compresses to `'3a'`
- `'cc'` compresses to `'2c'`
- `'t'` remains `'t'`

The input string consists only of alphabetic characters (lowercase and/or uppercase).

---

## Solution Explanation

To solve this problem, we use the **two pointers** method, which is both efficient and easy to implement. Here's a breakdown of the solution:

### Steps:
1. **Append a sentinel character** (`'!'`) to the end of the string. This ensures the last group of characters is processed correctly without requiring additional checks.
2. Initialize two pointers:
   - `i` to track the start of the current group of characters.
   - `j` to iterate through the string and find where the current group ends.
3. Traverse the string:
   - If `s[i] == s[j]`, increment `j` to extend the current group.
   - If `s[i] != s[j]`, calculate the length of the group (`j - i`):
     - If the length is `1`, append the single character to the result.
     - If the length is greater than `1`, append the count and the character.
   - Update `i` to `j` to start processing the next group.
4. Finally, join all elements in the result list into a single string and return it.

---

## Code Implementation

```python
def compress(s):
    # Append a sentinel character to handle the last group of characters
    s += '!'
    result = []
    i = 0
    j = 0
    
    while j < len(s):
        if s[i] == s[j]:
            j += 1  
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num)) 
                result.append(s[i])
            i = j
    
    return ''.join(result)
```
## Time and Space Complexity

### Time Complexity:
- **O(n)**: The solution involves a single traversal of the string using the `j` pointer. Each character is processed once, making the algorithm linear in time complexity.

### Space Complexity:
- **O(n)**: The result list stores the compressed string, which in the worst case could be of the same size as the input string.

---

``` python
# Test Case 1
print(compress('ccaaatsss'))  # -> '2c3at3s'

# Test Case 2
print(compress('ssssbbz'))  # -> '4s2bz'

# Test Case 3
print(compress('ppoppppp'))  # -> '2po5p'

# Test Case 4
print(compress('nnneeeeeeeeeeeezz'))  # -> '3n12e2z'

# Test Case 5
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')) 
# -> '127y'
```

## Key Insights
- The two pointers method is ideal for problems involving contiguous groups of characters or numbers, as it allows efficient processing of such patterns.
- Adding a sentinel character simplifies edge case handling, particularly for the last group of characters.
- This approach avoids unnecessary intermediate computations, ensuring both clarity and performance