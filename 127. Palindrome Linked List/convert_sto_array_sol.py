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


# Convert To Array Solution:
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l, r = l + 1, r - 1

        return True

# Time Complexity: O(n), where n is the length of the linked list. In this solution, we traverse the linked list twice: once to convert it to an array and once to check if the array is a palindrome.
# Space Complexity: O(n), as we are using an array to store the values of the linked list.
# This solution is not optimal in terms of space complexity, as it requires O(n) additional space for the array.


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