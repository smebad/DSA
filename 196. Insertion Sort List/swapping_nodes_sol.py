# Insertion Sort List
# Swapping Nodes Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue

            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next

            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next
    
# Time complexity: O(n^2) in the worst case, where n is the number of nodes in the linked list. This occurs when the input list is sorted in reverse order.
# Space complexity: O(1) since we are using a constant amount of extra space.
# This swapping nodes solution efficiently sorts the linked list using insertion sort by rearranging the node pointers without creating new nodes.


# Test Cases
def print_list(head: Optional[ListNode]):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Test Case 1:
head1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head1 = Solution().insertionSortList(head1)
print_list(sorted_head1)  # Output: [1, 2, 3, 4]

# Test Case 2:
head2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
sorted_head2 = Solution().insertionSortList(head2)
print_list(sorted_head2)  # Output: [-1, 0, 3, 4, 5]
