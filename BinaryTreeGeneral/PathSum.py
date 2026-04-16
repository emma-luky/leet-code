# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def bfs(node, currSum):
            if node:
                currSum += node.val
                if node.right == None and node.left == None:
                    if currSum == targetSum:
                        return True
                    else:
                        return False
                return bfs(node.right, currSum) or bfs(node.left, currSum)
            return False
        if root:
            return bfs(root, 0)
        else:
            return False
