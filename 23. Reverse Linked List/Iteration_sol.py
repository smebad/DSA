# Reverse Linked List
# Iterative solution:

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
# Time complexity: O(n) for n nodes in the list
# Space complexity: O(1) for the iterative approach
# This iterative solution reverses the list in place without using extra space for recursion.

# Test Cases:

# Helper functions (only for testing)
def create_linked_list(arr):
    head = None
    for val in reversed(arr):
        head = ListNode(val, head)
    return head

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Test Case 1:
head = create_linked_list([1,2,3,4,5])
sol = Solution()
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))  # Output: [5,4,3,2,1]

# Test Case 2:
head = create_linked_list([1,2])
sol = Solution()
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))  # Output: [2,1]

# Test Case 3:
head = create_linked_list([])
sol = Solution()
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))  # Output: []
