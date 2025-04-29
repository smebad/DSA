# Reorder List
# Brute force solution:

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None

# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once to store the nodes in a vector and then again to reorder them.
# Space Complexity: O(n), where n is the number of nodes in the linked list. We use a vector to store the nodes.
# This solution is not optimal in terms of space complexity, as it uses O(n) additional space to store the nodes. A more optimal solution would be to use O(1) space by rearranging the nodes in place.
# However, this brute force solution is easier to understand and implement, especially for beginners.


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
