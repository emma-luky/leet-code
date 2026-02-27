# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minimum = float('inf')

        def inorder(curr):
            if curr:
                inorder(curr.left)
                if self.prev is not None:
                    difference = abs(self.prev.val - curr.val)
                    self.minimum = min(difference, self.minimum)
                self.prev = curr
                inorder(curr.right)

        inorder(root)
        return self.minimum
