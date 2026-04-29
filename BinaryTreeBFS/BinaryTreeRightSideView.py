# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            queue = deque([root])
            res = []
            while queue:
            # Save the current number of nodes in the queue (size of the current level).
            # Pop all nodes of this level, enqueuing their left and right children.
            # After finishing the level, if the queue still holds nodes (the next level),
            # the last element in the queue is the rightmost node of that level – append its value
                size = len(queue)
                res.append(queue[size - 1].val)
                for i in range(size):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return res
        return []
