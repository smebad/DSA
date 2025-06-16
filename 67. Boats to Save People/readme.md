# Boats to Save People - LeetCode

## Problem Description

The **Boats to Save People** problem asks us to find the minimum number of boats required to rescue all people, where:

* Each person has a specific weight given in an array `people`.
* Each boat can carry **at most two people** at the same time.
* The total weight on a boat **must not exceed** the given `limit`.
* We have an **infinite number of boats** available.

### Example 1:

* Input: `people = [1, 2]`, `limit = 3`
* Output: `1`
* Explanation: One boat can carry both 1 and 2 (total = 3).

### Example 2:

* Input: `people = [3, 2, 2, 1]`, `limit = 3`
* Output: `3`
* Explanation: Possible groupings - (3), (2,1), (2)

### Example 3:

* Input: `people = [3, 5, 3, 4]`, `limit = 5`
* Output: `4`
* Explanation: Each person must go individually as no pair fits under the limit.

### Constraints:

* `1 <= people.length <= 5 * 10^4`
* `1 <= people[i] <= limit <= 3 * 10^4`

---

## Solution: Two Pointers + Sorting

```python
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sort people by weight
        res, l, r = 0, 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]  # Remaining capacity after putting heaviest person
            r -= 1  # Always use a boat for the heaviest person
            res += 1  # Increment boat count

            if l <= r and remain >= people[l]:
                l += 1  # Pair the lightest person if possible

        return res
```

### Code Explanation (Commented)

* We **sort the array** to work with the lightest and heaviest people efficiently.
* Initialize two pointers:

  * `l` for the lightest person.
  * `r` for the heaviest person.
* Use a `while` loop until all people are assigned boats.
* In each iteration:

  * Put the heaviest unassigned person on a boat.
  * Try to pair with the lightest unassigned person **if they both fit**.
  * Always increase the boat count (`res`).

---

## Approach and Logic

The **goal** is to **minimize boats** by pairing the heaviest person with the lightest person whenever possible.

### Step-by-Step Logic:

1. **Sort** the weights to easily find optimal pairs.
2. **Two pointers** help track both ends of the sorted list.
3. Always assign a boat to the **heaviest unassigned person**.
4. **Try pairing** with the lightest person if total weight <= limit.
5. Repeat until all people are placed.

---

## Differences Between Approaches

* **Brute Force** (not shown here): Try all combinations (O(n^2)), very slow.
* **Optimal Approach**: Sort and two-pointer method. Efficient, easy to implement, no extra space.

---

## Time and Space Complexity

* **Time Complexity**: `O(n log n)`

  * Sorting takes `O(n log n)`
  * Two-pointer traversal takes `O(n)`
* **Space Complexity**: `O(1)`

  * In-place manipulation using pointers
  * No extra arrays or hash maps needed

---

## Why This is Optimal

* It balances time and space efficiency.
* Simple yet powerful logic using sorting and greedy pairing.
* Works well even for large inputs up to 50,000 people.

---

## Test Cases

```python
# Test Case 1
print(Solution().numRescueBoats([1,2], 3))  # Expected Output: 1

# Test Case 2
print(Solution().numRescueBoats([3,2,2,1], 3))  # Expected Output: 3

# Test Case 3
print(Solution().numRescueBoats([3,5,3,4], 5))  # Expected Output: 4
```

---

## Final Notes

* The greedy strategy used here works because we're always ensuring that the heaviest person is placed and we try to fit one more person only if possible.
* Sorting upfront unlocks an efficient way to make the best pairing choices using two pointers.
