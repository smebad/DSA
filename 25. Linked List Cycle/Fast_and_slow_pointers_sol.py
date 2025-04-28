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
 

# Fast and slow pointers solution:
from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. In the worst case, we traverse the list once.
# Space Complexity: O(1), as we are using only two pointers (slow and fast) to traverse the list.
# This is an efficient solution that uses the Floyd's Tortoise and Hare algorithm to detect cycles in a linked list. It is optimal in terms of both time and space complexity.
# What is Floyd's Tortoise and Hare algorithm? Floyd's Tortoise and Hare algorithm is a pointer algorithm that uses two pointers, one moving at twice the speed of the other. If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.
# However, this algorithm is more complex to implement than the hash set solution. It is also less intuitive, as it requires a deeper understanding of pointer manipulation and cycle detection algorithms.
# This solution is a good choice for large linked lists, where memory usage is a concern. It is also optimal in terms of time and space complexity.

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