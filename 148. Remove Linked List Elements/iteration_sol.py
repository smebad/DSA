# Remove Linked List Elements
# Iteration Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt

        return dummy.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. This is because we traverse each node exactly once.
# Space Complexity: O(1) since we are using only a constant amount of extra space.
# This iterative approach uses a dummy node to simplify edge cases, such as removing the head node. It maintains two pointers, prev and curr, to track the previous and current nodes while traversing the list.

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
