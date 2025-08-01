# Reverse Linked List
# Recursion solution:

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
    
# Time complexity: O(n) for n nodes in the list 
# Space complexity: O(n) for the recursion stack
# This recursion reverses the list in place, but it uses O(n) space for the recursion stack.


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
