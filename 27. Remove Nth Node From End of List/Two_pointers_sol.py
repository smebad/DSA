# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


# Two Pointers solution:
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    
# Time complexity: O(N), where N is the number of nodes in the linked list.
# Space complexity: O(1), as we are using only a constant amount of space.
# This is the most efficient solution for this problem.
# This is because we are not using any extra space to store the nodes.
# The brute force solution is less efficient because it uses O(N) space to store the nodes. However, it is easier to understand and implement.
# The two pointers solution is more efficient because it uses O(1) space and O(N) time complexity.


# Test Cases:
# Helper function to create a linked list from a vector
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Test case 1
head1 = create_linked_list([1, 2, 3, 4, 5])
n1 = 2
solution = Solution()
result1 = solution.removeNthFromEnd(head1, n1)
# Print the result
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
print_linked_list(result1) # Test case 1 output: 1 -> 2 -> 3 -> 5 -> None

# Test case 2
head2 = create_linked_list([1])
n2 = 1
result2 = solution.removeNthFromEnd(head2, n2)
print_linked_list(result2) # Test case 2 output: None

# Test case 3
head3 = create_linked_list([1, 2])
n3 = 1
result3 = solution.removeNthFromEnd(head3, n3)
print_linked_list(result3) # Test case 3 output: 1 -> None
