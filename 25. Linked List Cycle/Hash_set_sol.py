# Linked List Cycle
# Hash set solution:

from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once, adding each node to the set.
# Space Complexity: O(n), where n is the number of nodes in the linked list. We store each node in the set.
# This is a trade-off between time and space complexity. The hash set solution is easier to understand and implement, but it uses more memory. If memory usage is a concern, we can use the Floyd's Tortoise and Hare algorithm, which uses O(1) space but is more complex to implement.
# The hash set solution is a good choice for small to medium-sized linked lists, where memory usage is not a major concern. It is also easier to understand and implement than the Floyd's Tortoise and Hare algorithm.

# Test Cases:
# Helper function to create a linked list with a cycle
def create_cycle_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    cycle_node = None
    for i in range(1, len(values)):
        cur.next = ListNode(values[i])
        cur = cur.next
        if i == pos:
            cycle_node = cur
    if cycle_node:
        cur.next = cycle_node  # Create a cycle
    return head

# Test case 1: Cycle exists
head1 = create_cycle_list([3, 2, 0, -4], 1)
solution1 = Solution()
print(solution1.hasCycle(head1))  # Output: True


# Test case 2: Cycle exists
head2 = create_cycle_list([1, 2], 0)
solution2 = Solution()
print(solution2.hasCycle(head2))  # Output: True

# Test case 3: No cycle
head3 = create_cycle_list([1], -1)
solution3 = Solution()
print(solution3.hasCycle(head3))  # Output: False
