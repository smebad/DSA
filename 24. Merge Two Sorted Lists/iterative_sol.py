# Merge Two Sorted Lists
# Iterative solution:

from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
        
# Time complexity: O(n + m), where n and m are the lengths of the two lists.
# Space complexity: O(1), since we are using a constant amount of space for the dummy node and the merged list.
# The merged list is created in place without using any additional data structures.
# This iterative approach is more efficient than the recursive approach in terms of space complexity.
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

