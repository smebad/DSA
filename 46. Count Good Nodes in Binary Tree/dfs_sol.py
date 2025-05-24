# Count Good Nodes in Binary Tree
# Depth First Search Solution:

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
    
# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
# Space Complexity: O(h), where h is the height of the binary tree. This is due to the recursion stack used in the DFS traversal.
# The space complexity can be O(n) in the worst case of a skewed tree, but on average it is O(log n) for balanced trees.
# This solution efficiently counts the good nodes by traversing the tree and keeping track of the maximum value seen so far in the path from the root to the current node. Each time it encounters a node that is greater than or equal to this maximum value, it counts it as a good node.


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
