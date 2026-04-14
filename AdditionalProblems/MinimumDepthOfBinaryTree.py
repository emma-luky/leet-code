# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(node, count):
            if node.left == None and node.right == None:
                return count
            if node.left and node.right:
                return min(bfs(node.left, count + 1), bfs(node.right, count + 1))
            if node.left:
                return bfs(node.left, count + 1)
            if node.right:
                return bfs(node.right, count + 1)
        if root:
            return bfs(root, 1)
        else:
            return 0        
