# Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50


# Recursion Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We visit each node exactly once.
# Space Complexity: O(n) in the worst case due to the recursion stack. In the best case (when no nodes are removed), the space complexity is O(1).
# This recursive approach is elegant and leverages the call stack to handle the linked list traversal and modification.

# Test Cases:
def print_linked_list(head: Optional[ListNode]):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val1 = 6  
expected1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = Solution().removeElements(head1, val1)
print_linked_list(result1)  # Output: [1, 2, 3, 4, 5]

# Test Case 2
head2 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val2 = 7
expected2 = None
result2 = Solution().removeElements(head2, val2)
print_linked_list(result2)  # Output: []

# Test Case 3
head3 = None
val3 = 7
expected3 = None
result3 = Solution().removeElements(head3, val3)
print_linked_list(result3)  # Output: []