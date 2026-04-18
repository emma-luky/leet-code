# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indicies = {}
        for i in range(len(inorder)):
            indicies[inorder[i]] = i
        def build(start, end):
            if start > end:
                return
            node = TreeNode(postorder.pop())
            index = indicies[node.val]
            node.right = build(index + 1, end)
            node.left = build(start, index - 1)
            return node
        return build(0, len(postorder) - 1)
