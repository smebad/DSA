# Remove K Digits - LeetCode

## 1. Problem Explanation

**Remove K Digits** is a classic greedy + stack problem where you are given:

* A string `num` representing a non-negative integer
* An integer `k`

Your task is to remove **exactly `k` digits** from `num` so that the resulting number is **as small as possible**.

### Important Rules

* The relative order of the remaining digits must be preserved
* The final result must **not contain leading zeros**
* If all digits are removed, return `"0"`

---

## 2. Code With Comments

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # This stack will store digits of the final number

        # Traverse each digit in the number
        for c in num:
            # Remove digits from stack if:
            # 1) We still have digits to remove (k > 0)
            # 2) Stack is not empty
            # 3) Top of stack is greater than current digit
            # This ensures we build the smallest possible number
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()

            # Add the current digit to the stack
            stack.append(c)

        # If k is still greater than 0, remove digits from the end
        # This happens when the number is already increasing
        stack = stack[:len(stack) - k]

        # Convert stack to string
        res = "".join(stack)

        # Remove leading zeros by converting to int
        # Return "0" if the result is empty
        return str(int(res)) if res else "0"
```

---

## 3. Solution Approach and Logic

### Key Idea

To get the **smallest possible number**, we want **smaller digits to appear earlier**. If a larger digit appears before a smaller one, it should be removed if possible.

This naturally leads to a **monotonic increasing stack** strategy.

---

### Step-by-Step Logic

1. Traverse the number digit by digit
2. Maintain a stack that is always **in increasing order**
3. If the current digit is smaller than the stack’s top:

   * Pop from the stack
   * Decrease `k`
4. Push the current digit into the stack
5. After traversal:

   * If `k > 0`, remove digits from the end
6. Remove leading zeros and return the result

---

### Why the Stack Works

* The stack ensures that bigger digits are removed **before** smaller digits
* This greedy removal guarantees the smallest lexicographical number

Example:

```
num = "1432219", k = 3
Stack operations:
1 → [1]
4 → [1,4]
3 → pop 4 → [1,3]
2 → pop 3 → [1,2]
2 → [1,2,2]
1 → pop 2 → [1,2,1]
9 → [1,2,1,9]
Result: 1219
```

---

## 4. Time and Space Complexity

### Time Complexity

* **O(n)**
* Each digit is pushed and popped at most once

### Space Complexity

* **O(n)**
* Stack may store all digits in the worst case

---

## 5. Why This Solution Is Optimal

* It processes the input in one pass
* No backtracking or repeated checks
* Uses greedy decisions that are mathematically optimal
* Handles edge cases like leading zeros and full deletion correctly

This is the most optimal solution under the given constraints.

---

## 6. Test Cases

```python
solution = Solution()

print(solution.removeKdigits("1432219", 3))  # 1219
print(solution.removeKdigits("10200", 1))    # 200
print(solution.removeKdigits("10", 2))       # 0
print(solution.removeKdigits("123456", 3))   # 123
print(solution.removeKdigits("7654321", 4))  # 321
```