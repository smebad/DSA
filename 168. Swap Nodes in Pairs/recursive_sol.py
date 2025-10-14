# Swap Nodes in Pairs
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
