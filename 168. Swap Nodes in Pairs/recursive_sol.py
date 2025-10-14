# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:



# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


# Recursive Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head
        nxt = head.next
        cur.next = self.swapPairs(nxt.next)
        nxt.next = cur
        return nxt
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We visit each node exactly once.
# Space Complexity: O(n) due to the recursion stack. In the worst case, the recursion depth can go up to n/2, which is O(n).
# This recursive approach is elegant and leverages the call stack to handle the swapping of nodes in pairs.


# Test Cases:
solution = Solution()

# Test Case 1:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = solution.swapPairs(head)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)  # Output: 2 1 4 3

# Test Case 2:
head = None
result = solution.swapPairs(head)
print(result)  # Output: None

# Test Case 3:
head = ListNode(1)
result = solution.swapPairs(head)
print(result.val)  # Output: 1

# Test Case 4:
head = ListNode(1, ListNode(2, ListNode(3)))
result = solution.swapPairs(head)
print(result.val, result.next.val, result.next.next.val)  # Output: 2 1 3