# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


# Convert To Array solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        return arr[len(arr) // 2]
    
# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the entire linked list once to convert it into an array.
# Space Complexity: O(n), since we are using an array to store all the nodes of the linked list.
# This array solution is straightforward and easy to implement, but it uses extra space.


# Test Cases:
solution = Solution()

# Test Case 1:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = solution.middleNode(head)
print(result.val)  # Output: 3
print(result.next.val)  # Output: 4
print(result.next.next.val)  # Output: 5

# Test Case 2:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
result = solution.middleNode(head)
print(result.val)  # Output: 4
print(result.next.val)  # Output: 5
print(result.next.next.val)  # Output: 6