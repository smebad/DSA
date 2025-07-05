# Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

# Follow up: Could you do it in one pass?


# Iteration solution:
# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head

        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next
    
# Time Complexity: O(n) where n is the number of nodes in the linked list. This is because we traverse the list a constant number of times, specifically once to reach the left position and once to reverse the nodes between left and right. We also traverse the list once to connect the reversed sublist to the rest of the list.
# Space Complexity: O(1) since we are using a constant amount of extra space (only a few pointers) regardless of the size of the input linked list.
# This solution is efficient and meets the problem's constraints.


# Test Cases
# Test Case 1:
# Create the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

left = 2
right = 4

sol = Solution()
new_head = sol.reverseBetween(head, left, right)

# Print result
while new_head:
    print(new_head.val, end=" ")  # Output should be: 1 4 3 2 5
    new_head = new_head.next
print()  # For a new line after the output

# Create the linked list [5]
head2 = ListNode(5)
left2 = 1
right2 = 1

new_head2 = sol.reverseBetween(head2, left2, right2)

# Print result
while new_head2:
    print(new_head2.val, end=" ")  # Output should be: 5
    new_head2 = new_head2.next

