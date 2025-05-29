# Last Stone Weight - LeetCode

## Problem Description

The **Last Stone Weight** problem simulates a game where stones with positive integer weights are smashed together according to specific rules:

1. In each round, select the two **heaviest** stones.
2. If they are **equal**, both are destroyed.
3. If they are **not equal**, the smaller one is destroyed, and the larger one is replaced by the difference of their weights.
4. Repeat the process until one or no stones are left.

The goal is to return the **weight of the last remaining stone**, or `0` if all stones are destroyed.

### Example 1:

```text
Input:  stones = [2, 7, 4, 1, 8, 1]
Output: 1
Explanation:
- Smash 7 and 8 -> get 1, array becomes [2, 4, 1, 1, 1]
- Smash 2 and 4 -> get 2, array becomes [2, 1, 1, 1]
- Smash 2 and 1 -> get 1, array becomes [1, 1, 1]
- Smash 1 and 1 -> get 0, array becomes [1]
Result: 1
```

### Example 2:

```text
Input:  stones = [1]
Output: 1
```

### Constraints:

* `1 <= stones.length <= 30`
* `1 <= stones[i] <= 1000`

---

## Sorting-Based Solution

```python
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()  # Sort stones to get the two largest
            cur = stones.pop() - stones.pop()  # Subtract the two heaviest
            if cur:
                stones.append(cur)  # Add the result back if not zero
        return stones[0] if stones else 0
```

### Explanation:

* We sort the list each time to access the two heaviest stones.
* Pop the last two elements (which are the heaviest due to sorting).
* Compute their difference. If not zero, add the result back.
* Continue until one or no stones remain.

### Time & Space Complexity:

* **Time Complexity:** O(n^2 log n)

  * Sorting happens every iteration and we could do this up to n times.
* **Space Complexity:** O(1) if modifying the input list in-place; otherwise, O(n).

### Drawback:

* Repeated sorting is inefficient for larger input sizes. Acceptable for constraints (up to 30 elements).

---

## Heap-Based (Optimal) Solution

```python
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]  # Use negatives to simulate max-heap
        heapq.heapify(stones)  # Convert list into a heap

        while len(stones) > 1:
            first = heapq.heappop(stones)  # Heaviest
            second = heapq.heappop(stones)  # Second heaviest
            if second > first:
                heapq.heappush(stones, first - second)  # Push the difference back

        stones.append(0)  # Add zero in case heap is empty
        return abs(stones[0])
```

### Explanation:

* Python has a min-heap by default, so we invert stone weights using negatives.
* Heaviest stones become the smallest negative numbers.
* Use `heapq.heappop` to pop the two heaviest stones.
* If they are not equal, push the difference back (still as negative).
* If only one stone remains, return its absolute value.

### Time & Space Complexity:

* **Time Complexity:** O(n log n)

  * Heapify takes O(n), and each push/pop is O(log n).
* **Space Complexity:** O(n)

  * We store all stones in a heap.

---

## Comparison of Solutions

| Feature          | Sorting Solution      | Heap Solution (Optimal)  |
| ---------------- | --------------------- | ------------------------ |
| Time Complexity  | O(n^2 log n)          | O(n log n)               |
| Space Complexity | O(n)                  | O(n)                     |
| Speed            | Slower due to sorting | Faster due to heap usage |
| Code Simplicity  | Simpler to understand | Slightly more advanced   |
| Use Case         | Small inputs          | Large or dynamic inputs  |

---

## Conclusion

* For beginners or very small inputs, the **sorting solution** is easier to implement.
* For optimal performance, especially with frequent or large inputs, the **heap-based solution** is preferred.
* The heap allows for more efficient retrieval and insertion of the largest elements, which fits this problem's needs perfectly.

---

## Test Cases

```python
# Test Case 1
stones = [2, 7, 4, 1, 8, 1]
print(Solution().lastStoneWeight(stones))  # Expected Output: 1

# Test Case 2
stones = [1]
print(Solution().lastStoneWeight(stones))  # Expected Output: 1
```
