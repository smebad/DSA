#  Merge In Between Linked Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = 0

        while i < a - 1:
            curr = curr.next
            i += 1
        head = curr

        while i <= b:
            curr = curr.next
            i += 1

        head.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = curr

        return list1
    
# Time complexity: O(N + M) where N is the length of list1 and M is the length of list2. We iterate through both lists once.
# Space complexity: O(1) since we are modifying the lists in place and not using any additional data structures.
# This solution efficiently merges list2 into list1 between the ath and bth nodes using two pointers.


# Test Cases
def print_linked_list(head):
    curr = head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(result)

# Test Case 1
list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
a = 3
b = 4
result = Solution().mergeInBetween(list1, a, b, list2)
print_linked_list(result)  # Expected Output: [10, 1, 13, 1000000, 1000001, 1000002, 5]

# Test Case 2
list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004)))))
a = 2
b = 5
result = Solution().mergeInBetween(list1, a, b, list2)
print_linked_list(result)  # Expected Output: [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
