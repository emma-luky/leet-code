# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(node, arr):
            if node:
                inorder(node.left, arr)
                arr.append(node.val)
                inorder(node.right, arr)
            return arr
        arr1 = inorder(root1, [])
        arr2 = inorder(root2, [])
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        while i < len(arr1):
            ans.append(arr1[i])
            i += 1
        while j < len(arr2):
            ans.append(arr2[j])
            j += 1
        return ans
