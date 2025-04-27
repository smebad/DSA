# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Recursive solution:
from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
# Time complexity: O(n + m), where n and m are the lengths of the two lists.
# Space complexity: O(n + m), where n and m are the lengths of the two lists.
# This is due to the recursion stack space used in the function calls.
# The space complexity can be reduced to O(1) if we use an iterative approach instead of recursion.
# However, the recursive approach is more elegant and easier to understand.


# Test Cases:
# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test Case 1:
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)
# Print merged list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
print_linked_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

# Test Case 2:
list1 = create_linked_list([])
list2 = create_linked_list([])
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)
# Print merged list
print_linked_list(merged_list)  # Output: None

# Test Case 3:
list1 = create_linked_list([])
list2 = create_linked_list([0])
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)
# Print merged list
print_linked_list(merged_list)  # Output: 0 -> None

