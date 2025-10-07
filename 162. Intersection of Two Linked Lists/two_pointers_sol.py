# Intersection of Two Linked Lists
# Two Pointers solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

# Time Complexity: O(m + n), where m and n are the lengths of the two linked lists. In the worst case, we traverse both lists entirely.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the two pointers.
# This two-pointer technique ensures that both pointers traverse the same total distance, which leads them to meet at the intersection point if one exists. If there is no intersection, both pointers will eventually become null at the same time, and we return null.


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

