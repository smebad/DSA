# Add Two Numbers
# Iterative solution:

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
# Time complexity: O(m + n), where m and n are the lengths of the two linked lists. 
# Space complexity: O(1), O(max(m, n)) if we consider the output linked list as part of the input.
# The space complexity is O(1) if we do not consider the output linked list as part of the input.
# This solution is efficient in terms of both time and space complexity and can be difficult to understand but this is the best solution for this problem.


# Test Cases
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test case 1
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: [7, 0, 8]

# Test case 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = Solution().addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: [0]

# Test case 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = Solution().addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
