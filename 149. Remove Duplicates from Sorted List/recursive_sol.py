# Remove Duplicates from Sorted List
# Recursive Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)
        return head if head.val != head.next.val else head.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We visit each node exactly once.
# Space Complexity: O(n) in the worst case due to the recursion stack. In the best case (no duplicates), the space complexity is O(1).
# This recursive approach effectively removes duplicates by leveraging the call stack to handle the linked list traversal.

# Test Cases:
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test Case 1:
head = ListNode(1, ListNode(1, ListNode(2)))
print_list(Solution().deleteDuplicates(head))  # Output: 1 -> 2 -> None

# Test Case 2:
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print_list(Solution().deleteDuplicates(head))  # Output: 1 -> 2 -> 3 -> None
