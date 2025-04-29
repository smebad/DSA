# Reorder List
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]


# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Reverse and merge solution:
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list a few times, but each traversal is O(n).
# Space Complexity: O(1), as we are rearranging the nodes in place without using any additional data structures.
# This solution is optimal in terms of both time and space complexity, as it uses O(n) time to traverse the list and O(1) space to rearrange the nodes.
# This reverse and merge solution is efficient and works well for large linked lists. It uses the two-pointer technique to find the middle of the list, reverses the second half, and then merges the two halves in the required order.


# Test cases:
# Helper function to create a linked list from a vector
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test case 1:
head1 = create_linked_list([1, 2, 3, 4])
solution = Solution()
solution.reorderList(head1)
# Print the reordered list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
print_linked_list(head1)  # Output: 1 -> 4 -> 2 -> 3 -> None

# Test case 2:
head2 = create_linked_list([1, 2, 3, 4, 5])
solution.reorderList(head2)
# Print the reordered list
print_linked_list(head2)  # Output: 1 -> 5 -> 2 -> 4 -> 3 -> None

# Test case 3:
head3 = create_linked_list([1])
solution.reorderList(head3)
# Print the reordered list
print_linked_list(head3)  # Output: 1 -> None