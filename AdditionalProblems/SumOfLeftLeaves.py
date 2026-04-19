# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 1 means its left
        # 0 means its right
        def bfs(node, left):
            if node:
                if node.left or node.right:
                    return bfs(node.left, 1) + bfs(node.right, 0)
                else:
                    return node.val if left else 0
            else:
                return 0
        return bfs(root, 0)
