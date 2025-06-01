# Task Scheduler - LeetCode

## Problem Explanation

The **Task Scheduler** problem involves scheduling tasks labeled from **A to Z** in such a way that the same task is executed **at least `n` intervals apart**. During each interval, the CPU can either perform a task or remain idle.

**Goal**: Return the **minimum number of CPU intervals** required to complete all the tasks.

### Constraints:

* Tasks can be completed in any order.
* After executing a task, there must be a cooldown (idle or different tasks) of `n` intervals before the same task can be executed again.

### Example:

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B
```

---

## Code Explanation with Comments

```python
from collections import Counter, deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)

        # Use a max heap (invert frequencies to simulate max heap with Python's min-heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # queue to hold tasks that are cooling down, format: [remaining_count, ready_time]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                # If no task is available, skip to the next task's ready time
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)  # Execute a task
                if cnt:
                    q.append([cnt, time + n])  # Add to cooldown queue

            # If a task's cooldown is over, add it back to the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
```

---

## Solution Approach and Logic

### Step-by-Step Approach:

1. **Count the tasks**: Determine how often each task appears.
2. **Use a max heap**: Always pick the most frequent task first (to reduce idle time).
3. **Cooldown mechanism**: After executing a task, push it into a queue with a timestamp indicating when it can be used again.
4. **Cycle**:

   * Increment the time with every cycle.
   * Execute tasks from the heap if possible.
   * If the heap is empty, the CPU idles (time jumps to next available task).
   * Tasks re-enter the heap once their cooldown ends.

### Why Use Max Heap?

Using the most frequent task reduces idle time and maximizes efficiency. By handling tasks with the highest count first, we can distribute them optimally across the timeline.

---

## Test Cases

```python
# Test Case 1
tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))  # Expected Output: 8

# Test Case 2
tasks = ["A","C","A","B","D","B"]
n = 1
print(Solution().leastInterval(tasks, n))  # Expected Output: 6

# Test Case 3
tasks = ["A","A","A","B","B","B"]
n = 3
print(Solution().leastInterval(tasks, n))  # Expected Output: 10
```

---

## Time and Space Complexity

### Time Complexity:

* **O(m log m)** where `m` is the number of unique tasks. This is due to heap operations and queue management.
* Each task is pushed and popped from the heap or queue at most once.

### Space Complexity:

* **O(m)** for the heap and queue where `m` is the number of unique tasks.

---

## Most Optimal Solution

The max-heap solution is **optimal** for this problem. It:

* Ensures that high-frequency tasks are executed with minimum idle time.
* Uses efficient data structures like heap and queue to manage cooldowns.
* Avoids brute-force simulation or sorting-based approaches that may be less performant with larger inputs.

**Why Optimal?**

* Efficiently prioritizes tasks to reduce idle periods.
* Takes advantage of greedy strategy and max-heap properties.

This solution is scalable and performs well even with the upper input limits (up to 10,000 tasks).

---

## Summary

* This task scheduling problem is about minimizing CPU intervals while respecting cooldowns.
* Using a max-heap helps prioritize tasks efficiently.
* The logic revolves around distributing the most frequent tasks to reduce idles.
* Time-efficient and space-conscious solution that handles edge cases gracefully.
