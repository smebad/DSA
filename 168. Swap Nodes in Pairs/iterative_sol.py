# Swap Nodes in Pairs
# Iterative Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nxtPair = curr.next.next
            second = curr.next

            # Reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # Update pointers
            prev = curr
            curr = nxtPair

        return dummy.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
# Space Complexity: O(1) since we are using only a constant amount of extra space.
# This iterative approach is efficient and avoids the overhead of recursion.



# Test Cases:
solution = Solution()

# Test Case 1:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = solution.swapPairs(head)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)  # Output: 2 1 4 3

# Test Case 2:
head = None
result = solution.swapPairs(head)
print(result)  # Output: None

# Test Case 3:
head = ListNode(1)
result = solution.swapPairs(head)
print(result.val)  # Output: 1

# Test Case 4:
head = ListNode(1, ListNode(2, ListNode(3)))
result = solution.swapPairs(head)
print(result.val, result.next.val, result.next.next.val)  # Output: 2 1 3
