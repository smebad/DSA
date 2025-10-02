# Average Waiting Time - LeetCode

## Problem Explanation

The "Average Waiting Time" problem is about simulating the workflow of a single chef in a restaurant. Customers arrive at certain times and each order takes a fixed amount of preparation time. The chef can only work on one order at a time, and customers must wait until their order is completed.

You are given an array `customers`, where:

* `customers[i][0]` = arrival time of the i-th customer.
* `customers[i][1]` = time required to prepare the order.

The goal is to calculate the **average waiting time** for all customers, where:

```
waiting_time = (time when order is finished) - (arrival time)
```

Finally, return the average waiting time as a floating-point number.

---

## Example

### Example 1

Input: `customers = [[1,2],[2,5],[4,3]]`

* Customer 1: arrives at 1, order finishes at 3 → waiting time = 2
* Customer 2: arrives at 2, chef starts at 3, finishes at 8 → waiting time = 6
* Customer 3: arrives at 4, chef starts at 8, finishes at 11 → waiting time = 7

Average waiting time = (2 + 6 + 7) / 3 = **5.0**

### Example 2

Input: `customers = [[5,2],[5,4],[10,3],[20,1]]`

* Customer 1: waiting time = 2
* Customer 2: waiting time = 6
* Customer 3: waiting time = 4
* Customer 4: waiting time = 1

Average waiting time = (2 + 6 + 4 + 1) / 4 = **3.25**

---

## Solution Code with Comments

```python
from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0   # Tracks the current time when chef is done with all previous orders
        total = 0  # Tracks the total waiting time of all customers

        for arrival, order in customers:
            # If chef is still busy when customer arrives, customer must wait
            if time > arrival:
                total += time - arrival   # add waiting time (when chef starts - arrival)
            else:
                # If chef is idle before this customer arrives, reset time to arrival
                time = arrival

            total += order   # add the order preparation time
            time += order    # update chef's time when he finishes this order

        # Average waiting time = total waiting time / number of customers
        return total / len(customers)
```

---

## Explanation of the Approach

This solution simulates the process step by step:

1. **Track the chef's time:**

   * If the chef is still busy (`time > arrival`), the customer waits until the chef is free.
   * Otherwise, the chef starts immediately when the customer arrives.

2. **Track waiting time:**

   * Waiting time is calculated as the finish time of the order minus the arrival time.
   * We accumulate this waiting time for each customer.

3. **Compute the average:**

   * Divide the total waiting time by the number of customers.

---

## Why This Approach Works

* The arrival times are sorted, so we can simply process customers in order.
* At every step, we only need to know whether the chef is idle or busy.
* There is no need for complex data structures like heaps or queues because there is only one chef and orders are processed sequentially.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * We go through all customers once.
* **Space Complexity:** `O(1)`

  * Only a few variables are used regardless of input size.

---

## Most Optimal Solution

The above solution is already **optimal**:

* We must at least check each customer once, so `O(n)` is the best possible time complexity.
* We only use constant space, which cannot be improved further.

Therefore, the simulation approach is the most efficient solution.

---

## Test Cases

```python
solution = Solution()

# Test Case 1
customers1 = [[1,2],[2,5],[4,3]]
print(solution.averageWaitingTime(customers1))  # Expected: 5.0

# Test Case 2
customers2 = [[5,2],[5,4],[10,3],[20,1]]
print(solution.averageWaitingTime(customers2))  # Expected: 3.25

# Edge Case: Single customer
customers3 = [[1,3]]
print(solution.averageWaitingTime(customers3))  # Expected: 3.0
```
