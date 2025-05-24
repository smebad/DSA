# Count Good Nodes in Binary Tree
# Breadth First Search Solution:

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
		
        q.append((root,-float('inf')))

        while q:
            node,maxval = q.popleft()
            if node.val >= maxval:  
                res += 1
				
            if node.left:    
                q.append((node.left,max(maxval,node.val)))
            
            if node.right:
                q.append((node.right,max(maxval,node.val)))
                
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
# Space Complexity: O(n), where n is the maximum number of nodes at any level in the tree, which can occur in the queue during BFS.
# This solution uses a breadth-first search (BFS) approach to traverse the binary tree and count the good nodes. And it maintains a queue to explore each node level by level, checking if the current node is a good node based on the maximum value seen so far in the path from the root to that node.
# However, the depth-first search (DFS) solution is more efficient in terms of space complexity, as it uses recursion and does not require an additional queue structure.


# Test Cases:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

# Test Case 1
def test_case_1():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    
    solution = Solution()
    assert solution.goodNodes(root) == 4

# Test Case 2
def test_case_2():
    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    
    solution = Solution()
    assert solution.goodNodes(root) == 3

# Test Case 3
def test_case_3():
    root = TreeNode(1)
    
    solution = Solution()
    assert solution.goodNodes(root) == 1

# Run all tests
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    print("All test cases passed.")
