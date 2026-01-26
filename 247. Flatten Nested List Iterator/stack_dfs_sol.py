# Flatten Nested List Iterator
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.

 

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
 

# Constraints:

# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-106, 106].


# Stack solution:
# Class definition for NestedInteger
class NestedInteger:
    def __init__(self, value=None):
        if isinstance(value, int):
            self.value = value
            self.list = None
        else:
            self.value = None
            self.list = value or []

    def isInteger(self):
        return self.value is not None

    def getInteger(self):
        return self.value

    def getList(self):
        return self.list


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nested):
        for num in nested:
            if num.isInteger():
                self.stack.append(num.getInteger())
            else:
                self.dfs(num.getList())

# Time Complexity: O(n), where n is the total number of integers in the nested list. This is because we need to traverse all the elements in the nested list to flatten it.
# Space Complexity: O(n), where n is the total number of integers in the nested list. This is because we store all the integers in the stack.
# This implementation uses a depth-first search (DFS) approach to flatten the nested list and store the integers in a stack. The stack is then reversed to maintain the correct order for iteration. The next() method pops the top integer from the stack, and hasNext() checks if there are any integers left in the stack.


# Test Cases:
# Test Case 1:
nestedlist1 = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
i1 = NestedIterator(nestedlist1)
print(i1.next()) # Expected Output: 1
print(i1.next()) # Expected Output: 1
print(i1.next()) # Expected Output: 2
print(i1.next()) # Expected Output: 1
print(i1.next()) # Expected Output: 1
print(i1.hasNext()) # Expected Output: False