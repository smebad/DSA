# Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

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