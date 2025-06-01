# Task Scheduler
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100


# Max-Heap Solution:
from collections import Counter, deque
from typing import List
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
# Time complexity: O(m) where m is the number of unique tasks. This is because we use a hash map to count the frequency of each task. 
# Space complexity: O(1) since we use a constant number of variables. This includes the hash map and the max heap.
# The max heap is used to store the frequency of each task, so the space complexity is O(m) where m is the number of unique tasks.
# The deque is used to store the idle time for each task, so the space complexity is O(m) where m is the number of unique tasks.
# This Max Heap solution is efficient and works well within the constraints given (1 <= tasks.length <= 104, 0 <= n <= 100).


# Test Cases:
# Test Case 1:
tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n)) # Expected Output: 8

# Test Case 2:
tasks = ["A","C","A","B","D","B"]
n = 1
print(Solution().leastInterval(tasks, n)) # Expected Output: 6

# Test Case 3:
tasks = ["A","A","A", "B","B","B"]
n = 3
print(Solution().leastInterval(tasks, n)) # Expected Output: 10