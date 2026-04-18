# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = deque(preorder)
        # def build(preorder, inorder):
        #     if inorder:
        #         idx = inorder.index(preorder.popleft())
        #         node = TreeNode(inorder[idx])

        #         node.left = build(preorder, inorder[:idx])
        #         node.right = build(preorder, inorder[idx+1:])
        #         return node
        # return build(preorder, inorder)
        indicies = {}
        for i in range(len(inorder)):
            indicies[inorder[i]] = i
        queue = deque(preorder)
        def build(start, end):
            if start > end:
                return
            node = TreeNode(queue.popleft())
            mid = indicies[node.val]
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            return node
        return build(0, len(preorder) - 1)
