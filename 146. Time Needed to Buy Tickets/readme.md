# Time Needed to Buy Tickets - LeetCode

## Problem Explanation

The problem "Time Needed to Buy Tickets" is about simulating how long it will take for a specific person (at index `k`) in a queue to finish buying all their tickets.

* Each person in the queue needs a certain number of tickets (`tickets[i]`).
* Buying one ticket takes exactly **1 second**.
* After buying a ticket, if a person still needs more tickets, they instantly go to the end of the line.
* If a person has bought all their tickets, they leave the line.

The task is to compute the **total time (in seconds)** it takes for the person at index `k` to finish buying all their tickets.

---

### Example Walkthrough

#### Example 1:

Input: `tickets = [2, 3, 2], k = 2`

* Person 0 can buy `min(2, 2) = 2` tickets.
* Person 1 can buy `min(3, 2) = 2` tickets.
* Person 2 (kth person) can buy `min(2, 2) = 2` tickets.
* Total = 2 + 2 + 2 = **6 seconds**.

#### Example 2:

Input: `tickets = [5, 1, 1, 1], k = 0`

* Person 0 (kth person) buys `5` tickets.
* Person 1 can buy `min(1, 4) = 1`.
* Person 2 can buy `min(1, 4) = 1`.
* Person 3 can buy `min(1, 4) = 1`.
* Total = 5 + 1 + 1 + 1 = **8 seconds**.

---

## Code with Comments

```python
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0  # total time in seconds

        for i in range(len(tickets)):
            # If the person is before or at index k:
            # They can buy up to tickets[k] times, since person k is still in line.
            if i <= k:
                res += min(tickets[i], tickets[k])
            # If the person is after index k:
            # They can only buy up to (tickets[k] - 1) times, because person k finishes before them.
            else:
                res += min(tickets[i], tickets[k] - 1)

        return res
```

---

## Approach and Logic

### Step-by-step Explanation:

1. The person at index `k` needs `tickets[k]` tickets.
2. Every person before or at index `k` will get the chance to buy tickets **each time** person `k` is still waiting. So, they contribute at most `tickets[k]` seconds.
3. Every person **after** index `k` may not get the chance to buy all their tickets. This is because once person `k` finishes buying all their tickets, the process stops. So, their maximum contribution is `tickets[k] - 1` seconds.

---

## Time and Space Complexity

* **Time Complexity:** O(n), where `n` is the number of people in the queue. We go through the list once.
* **Space Complexity:** O(1), since we only use a constant amount of extra space.

---

## Optimal Solution

The iterative solution provided is the most optimal:

* It runs in **linear time O(n)**, which is efficient given the constraint (n ≤ 100).
* It uses only constant space.
* Other approaches, like simulating the queue step by step, would be less efficient (O(n × tickets\[k]) in worst case). This solution avoids unnecessary simulation by directly calculating contributions.

---

## Test Cases

```python
# Test Cases:
sol = Solution()

# Test Case 1:
tickets = [2, 3, 2]
k = 2
print(sol.timeRequiredToBuy(tickets, k))  # Output: 6

# Test Case 2:
tickets = [5, 1, 1, 1]
k = 0
print(sol.timeRequiredToBuy(tickets, k))  # Output: 8
```