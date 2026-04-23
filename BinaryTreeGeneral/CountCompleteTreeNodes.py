# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            if node:
                return 1 + bfs(node.right) + bfs(node.left)
            else:
                return 0
        return bfs(root)
