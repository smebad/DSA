# Depth First Search
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Depth First Search Solution:
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
          
          nodeP = q1.popleft()
          nodeQ = q2.popleft()

          if nodeP is None and nodeQ is None:
              continue
          if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
              return False

          q1.append(nodeP.left)
          q1.append(nodeP.right)
          q2.append(nodeQ.left)
          q2.append(nodeQ.right)

        return True
        

# Time Complexity: O(n) where n is the number of nodes in the tree. This is because we need to visit each root node once.
# Space Complexity: O(n) where n is the number of nodes in the tree. This is because we need to keep track of the nodes in the queue during the BFS traversal.
# This breadth first search solution is efficient and works well for both balanced and unbalanced trees.
# However, it uses more space compared to the depth first search solution due to the use of a queue.
# But both BFS and DFS solutions have the same time complexity of O(n) and are efficient for this problem.


# Test Cases:

# Test Case 1:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(Solution().isSameTree(root1, root2)) # True

# Test Case 2:
root3 = TreeNode(1)
root3.left = TreeNode(2)

root4 = TreeNode(1)
root4.right = TreeNode(2)

print(Solution().isSameTree(root3, root4)) # False

# Test Case 3:
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(1)

root6 = TreeNode(1)
root6.left = TreeNode(1)
root6.right = TreeNode(2)

print(Solution().isSameTree(root5, root6)) # False