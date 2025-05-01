# Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


# Hashmap + Two pass solution:
from typing import Optional
from typing import List, Union
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
    
# Time complexity: O(n), where n is the number of nodes in the linked list.
# Space complexity: O(n), where n is the number of nodes in the linked list. We use a hashmap to store the mapping between the original nodes and the copied nodes.
# This requires O(n) space in the worst case, where all nodes are unique and need to be stored in the hashmap.
# The space complexity can be reduced to O(1) if we don't use a hashmap, but that would require modifying the original list, which is not allowed in this problem. However, the hashmap + two-pass solution is more straightforward and easier to understand.


# Test cases:
def build_linked_list(data: List[List[Union[int, None]]]) -> Optional[Node]:
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]


def serialize_linked_list(head: Optional[Node]) -> List[List[Union[int, None]]]:
    result = []
    node_to_index = {}
    cur = head
    idx = 0
    while cur:
        node_to_index[cur] = idx
        cur = cur.next
        idx += 1
    cur = head
    while cur:
        rand_idx = node_to_index[cur.random] if cur.random else None
        result.append([cur.val, rand_idx])
        cur = cur.next
    return result


# -----------------------------
# Simple Test Runner
# -----------------------------

def test(input_data):
    print("Input:", input_data)
    head = build_linked_list(input_data)
    copied_head = Solution().copyRandomList(head)
    output = serialize_linked_list(copied_head)
    print("Copied:", output)
    print("-" * 40)


if __name__ == "__main__":
    test([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    test([[1, 1], [2, 1]])
    test([[3, None], [3, 0], [3, None]])
