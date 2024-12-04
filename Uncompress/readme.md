# Uncompress

## Problem Description

The `uncompress` function takes a string as an input that follows a specific format: `<number><char>`. Each group in the string consists of a number followed by a character. For example, the input `"2c3a1t"` represents the groups `2c`, `3a`, and `1t`.

The task is to return an "uncompressed" version of the string, where each character in a group is repeated according to the associated number. For the example `"2c3a1t"`, the output would be `"ccaaat"`.

You can assume the input string is well-formed.

---

## Solution: Two-Pointer Technique

### How it Works

The two-pointer technique is used to efficiently traverse the input string while extracting groups and constructing the uncompressed result:

1. **Pointers Initialization**:
   - `i`: Tracks the start of the current number.
   - `j`: Traverses the string to find the end of the current number and the associated character.

2. **Processing Groups**:
   - As `j` moves, it checks if the current character is numeric (indicating part of the number).
   - When `j` encounters a non-numeric character, it signals the end of a group.
   - Convert the substring between `i` and `j` (the number) into an integer and repeat the character `j` times.
   - Update `i` to the next starting point after processing the current group.

3. **Result Construction**:
   - Append the repeated characters to a result list.
   - At the end, join the list into a single string.

---

### Code Implementation

```python
def uncompress(s):
    numbers = '0123456789'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j
    return ''.join(result)
```

## Examples

| Input       | Output                  |
|-------------|-------------------------|
| `"2c3a1t"`  | `"ccaaat"`              |
| `"4s2b"`    | `"ssssbb"`              |
| `"2p1o5p"`  | `"ppoppppp"`            |
| `"3n12e2z"` | `"nnneeeeeeeeeeeezz"`   |
| `"127y"`    | `"y"` repeated 127 times |

---

## Time and Space Complexity

### Time Complexity:
- **n**: Number of groups in the string.
- **m**: Maximum number found in any group.

The function has a time complexity of **O(n * m)**:
- For each group (**n groups**), the character repetition takes **O(m)** time.

### Space Complexity:
- Since the output string stores repeated characters, the space complexity is also **O(n * m)**.

---

## Why Two Pointers?

The two-pointer approach ensures the string is traversed in a single pass (**O(n)** complexity for parsing), avoiding redundant operations like splitting the string or regex matching. This makes the solution both time-efficient and memory-efficient for well-formed input strings.

---

### Test Cases:
Here are some test cases to validate the implementation:
``` python
# Test Case 0
print(uncompress("2c3a1t"))  # -> 'ccaaat'

# Test Case 1
print(uncompress("4s2b"))  # -> 'ssssbb'

# Test Case 2
print(uncompress("2p1o5p"))  # -> 'ppoppppp'

# Test Case 3
print(uncompress("3n12e2z"))  # -> 'nnneeeeeeeeeeeezz'

# Test Case 4
print(uncompress("127y"))  # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
```

## Notes

- The function assumes that the input string is well-formed and contains no invalid characters or formatting.
- If the input format is unpredictable, additional validation logic should be added to handle edge cases.