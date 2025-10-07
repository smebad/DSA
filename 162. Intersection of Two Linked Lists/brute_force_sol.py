# Intersection of Two Linked Lists
# Brute Force solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA:
            cur = headB
            while cur:
                if headA == cur:
                    return headA
                cur = cur.next
            headA = headA.next
        return None

# TTime Complexity: O(m * n), where m and n are the lengths of the two linked lists. We have a nested loop where for each node in list A, we traverse the entire list B to check for intersection.
# Space Complexity: O(1), since we are using only a constant amount of extra space for the pointers.
# This brute force solution is straightforward but inefficient for large lists due to its quadratic time complexity.


# Test Case:
solution = Solution()

# Creating intersected linked lists
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)

# Intersecting the linked lists
headA.next.next.next.next.next = headB.next.next.next  # Node with value 8

result = solution.getIntersectionNode(headA, headB)
print(result.val)  # Output: 8

