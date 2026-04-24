# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        leaves = []
        def bfs(node, currNum):
            if node:
                currNum += str(node.val)
                if node.left == None and node.right == None:
                    leaves.append(currNum)
                if node.left:
                    bfs(node.left, currNum)
                if node.right:
                    bfs(node.right, currNum)
        bfs(root, "")
        ans = 0
        for leaf in leaves:
            ans += int(leaf)
        return ans
