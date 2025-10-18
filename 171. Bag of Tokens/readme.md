# Bag of Tokens - LeetCode

## Problem Explanation

The **"Bag of Tokens"** problem is a greedy algorithm challenge from LeetCode. You are given:

* A list of integers `tokens`, where each element represents the power value of a token.
* An integer `power`, representing your starting energy.

You also start with a **score of 0**. You can play each token **only once**, and in one of two ways:

1. **Face-Up Move:**

   * If your current power is **at least tokens[i]**, you can play the token face-up.
   * You **lose tokens[i] power** but **gain +1 score**.

2. **Face-Down Move:**

   * If your current score is **at least 1**, you can play the token face-down.
   * You **gain tokens[i] power** but **lose -1 score**.

Your goal is to maximize the **final score** by choosing the best sequence of plays.

---

## Example

### Example 1

**Input:**

```python
tokens = [100]
power = 50
```

**Output:**

```python
0
```

**Explanation:**
You cannot play the token face-up (not enough power) or face-down (score = 0). Hence, the result is 0.

### Example 2

**Input:**

```python
tokens = [200,100]
power = 150
```

**Output:**

```python
1
```

**Explanation:**
Play the 100 token face-up (power → 50, score → 1). You cannot play 200 face-up anymore.

### Example 3

**Input:**

```python
tokens = [100,200,300,400]
power = 200
```

**Output:**

```python
2
```

**Explanation:**

1. Play 100 face-up → power = 100, score = 1.
2. Play 400 face-down → power = 500, score = 0.
3. Play 200 face-up → power = 300, score = 1.
4. Play 300 face-up → power = 0, score = 2.

Maximum score = 2.

---

## Code Implementation (Two Pointers Solution)

```python
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        tokens.sort()  # Sort tokens to use smallest and largest efficiently
        l, r = 0, len(tokens) - 1  # Two pointers: left for smallest, right for largest

        while l <= r:
            # If we have enough power, play the smallest token face-up to gain score
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)  # Track maximum score reached
            # If not enough power, but we have a score, play the largest token face-down
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            # Otherwise, we cannot make any more moves
            else:
                break
        
        return res
```

---

## Step-by-Step Explanation

### 1. **Sorting the Tokens**

We first sort the tokens in ascending order. This allows us to:

* Use **smallest tokens** to gain score cheaply (face-up plays).
* Use **largest tokens** to regain power efficiently (face-down plays).

### 2. **Two-Pointer Strategy**

We use two pointers:

* `l` → points to the smallest unplayed token.
* `r` → points to the largest unplayed token.

We follow these rules:

* If you have enough power for `tokens[l]`, play it **face-up** → lose power, gain score.
* Otherwise, if you have a score to spare, play `tokens[r]` **face-down** → gain power, lose score.
* If neither move is possible, stop.

This ensures you are always making the most efficient move possible.

### 3. **Greedy Choice Logic**

The algorithm always prioritizes **gaining score when possible** and **regaining power only when stuck**. This greedy approach ensures the highest score.

---

## Time and Space Complexity

### Time Complexity: **O(n log n)**

* Sorting the tokens takes O(n log n).
* The two-pointer traversal takes O(n).
* Therefore, total = **O(n log n)**.

### Space Complexity: **O(1)**

* Only a few extra variables (`l`, `r`, `score`, `res`, and `power`) are used.
* Hence, space usage is constant.

---

## Why This is Optimal

This two-pointer greedy strategy is **optimal** because:

* Sorting ensures we always use minimal power first.
* The greedy exchange between smallest (for score) and largest (for power) tokens ensures maximum gain in both directions.
* Any other method, such as backtracking or simulation, would add unnecessary complexity without improving performance.

Thus, this solution achieves the **maximum possible score** efficiently using **O(n log n)** time and **O(1)** space.

## Test Cases
```python
solution = Solution()
# Test Case 1
tokens1 = [100]
power1 = 50
print(solution.bagOfTokensScore(tokens1, power1))  # Output: 0

# Test Case 2
tokens2 = [200, 100]
power2 = 150
print(solution.bagOfTokensScore(tokens2, power2))  # Output: 1

# Test Case 3
tokens3 = [100, 200, 300, 400]
power3 = 200
print(solution.bagOfTokensScore(tokens3, power3))  # Output: 2
```