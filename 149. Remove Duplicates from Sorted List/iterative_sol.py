# Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Iterative Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
# Space Complexity: O(1) since we are using only a constant amount of extra space.
# This iterative approach efficiently removes duplicates by maintaining a pointer to the current node and skipping over any duplicates. It is optimal for the problem at hand.


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