# Flatten Nested List Iterator - LeetCode

## 1. Problem Overview

The **Flatten Nested List Iterator** problem asks us to design an iterator that can traverse a deeply nested list of integers and return all integers in a flat, sequential order.

Each element in the input list is either:

* An integer, or
* A list that itself can contain integers or more lists

The goal is to build a class `NestedIterator` that supports two operations:

* `next()` returns the next integer in the flattened order
* `hasNext()` returns `true` if there are still integers left to read

### Example

Input: `[[1,1],2,[1,1]]`
Output: `[1,1,2,1,1]`

This means the iterator must walk through all levels of nesting and output numbers in left-to-right order.

---

## 2. Code with Comments

```python
class NestedInteger:
    def __init__(self, value=None):
        # If value is an integer, store it
        if isinstance(value, int):
            self.value = value
            self.list = None
        else:
            # Otherwise store it as a list
            self.value = None
            self.list = value or []

    def isInteger(self):
        return self.value is not None

    def getInteger(self):
        return self.value

    def getList(self):
        return self.list


class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        # Flatten the entire nested list using DFS
        self.dfs(nestedList)
        # Reverse the stack so we can pop from the end in correct order
        self.stack.reverse()
    
    def next(self):
        # Return the next integer from the flattened list
        return self.stack.pop()
    
    def hasNext(self):
        # Check if there are more integers left
        return len(self.stack) > 0

    def dfs(self, nested):
        # Traverse through the nested list
        for num in nested:
            if num.isInteger():
                # If it's an integer, store it
                self.stack.append(num.getInteger())
            else:
                # If it's a list, recursively flatten it
                self.dfs(num.getList())
```

---

## 3. Solution Explanation

This solution uses a **Depth First Search (DFS)** strategy to flatten the nested list.

### How it works

1. During initialization, we recursively traverse the entire nested list.
2. Every time we find an integer, we store it in a stack.
3. If we find a list, we recursively process it.
4. After flattening everything, we reverse the stack so that popping from the end gives the correct order.
5. `next()` simply pops an integer from the stack.
6. `hasNext()` checks if the stack is not empty.

### Why reversing is needed

DFS stores elements in the correct order but pushing them into a stack means the first element ends up at the bottom. Reversing fixes the order so popping works properly.

### Alternative Approach (not implemented here)

Another common solution uses a stack of iterators and flattens lazily instead of flattening everything at once. That approach saves memory but is more complex to implement.

---

## 4. Time and Space Complexity

Let **n** be the total number of integers in the nested list.

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(n)       |

### Why this is optimal

Every integer must be visited at least once, so O(n) time is unavoidable. Since this solution stores all integers, it also uses O(n) space. A lazy stack-based iterator can reduce space in some cases, but the time complexity remains O(n).

---

## 5. Summary and Test Case

This DFS-based solution is simple and efficient. It flattens the nested structure in one pass and allows fast `next()` and `hasNext()` operations afterward. It is easy to understand and ideal for learning how recursion and stacks work together in nested data problems.

```python
nestedlist1 = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
i1 = NestedIterator(nestedlist1)
print(i1.next()) # Expected Output: 1
print(i1.next()) # Expected Output: 1
print(i1.next()) # Expected Output: 2
print(i1.next()) # Expected Output: 1
print(i1.next()) # Expected Output: 1
print(i1.hasNext()) # Expected Output: False
```