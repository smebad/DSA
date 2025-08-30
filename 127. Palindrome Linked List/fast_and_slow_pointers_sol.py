# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?


# Fast and slow pointers Solution:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

# Time Complexity: O(n), where n is the length of the linked list. We traverse the list a few times, but each traversal is O(n).
# Space Complexity: O(1), as we are not using any additional data structures that grow with the input size.
# This solution is optimal in terms of both time and space complexity.


# Test Cases
sol = Solution()

# Test Case 1:
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
print(sol.isPalindrome(head1))  # Output: True

# Test Case 2:
head2 = ListNode(1)
head2.next = ListNode(2)
print(sol.isPalindrome(head2))  # Output: False